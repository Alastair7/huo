import asyncio
import discord
from discord.ext import commands
import youtube_dl

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn',
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source,volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')
    
    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url,download=not stream))

        if 'entries' in data:
            data = data['entries'[0]]
        
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='join', help="Joins bot to a voice channel.")
    async def join(self, ctx):
        if ctx.author.voice is None:
            embed = discord.Embed(description="You're not in a voice channel")
            await ctx.send(embed = embed)
        
        voiceChannel = ctx.author.voice.channel

        if ctx.voice_client is None:
            await voiceChannel.connect()
        else:
            await ctx.voice_client.move_to(voiceChannel)
    
    @commands.command(name='disconnect', help="Disconnect bot from a voice channel.")
    async def disconnect(self, ctx):
        vc = ctx.voice_client
        if vc.is_connected():
            await ctx.voice_client.disconnect()
        else:
            embed = discord.Embed(description="I am not connected in any voice channel!")
            await ctx.send(embed = embed)
    
    @commands.command(name='play', help="Play a song by URL from Youtube.")
    async def play(self, ctx,*, url : str):
        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.client.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
            embed = discord.Embed(description=f":arrow_forward: Now playing {player.title}")
            await ctx.send(embed = embed)

        
    @commands.command(name='pause', help="Pause a song.")
    async def pause(self, ctx):
        vc = ctx.voice_client
        if vc.is_playing():
            await ctx.voice_client.pause()
            embed = discord.Embed(description=f":pause_button: Song paused")
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(description="I am not playing anything!")
            await ctx.send(embed = embed)
    
    @commands.command(name='resume', help="Resume a song")
    async def resume(self, ctx):
        vc = ctx.voice_client
        if vc.is_paused():
            embed = discord.Embed(description=f":arrow_forward: Song resumed!")
            await ctx.voice_client.resume()
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(description="There's no music!")
            await ctx.send(embed = embed)
    
    @commands.command(name='stop', help = "Stop a song.")
    async def stop(self, ctx):
        vc = ctx.voice_client
        embed = discord.Embed(description=f":stop_button: Song stopped!")
        vc.stop()
        await ctx.send(embed = embed)
    

def setup(client):
    client.add_cog(Music(client))