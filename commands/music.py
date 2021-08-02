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
    'options': '-vn'
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
    
    @commands.command(name='join')
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("You're not in a voice channel!")
        
        voiceChannel = ctx.author.voice.channel

        if ctx.voice_client is None:
            await voiceChannel.connect()
        else:
            await ctx.voice_client.move_to(voiceChannel)
    
    @commands.command(name='disconnect')
    async def disconnect(self, ctx):
        vc = ctx.voice_client
        if vc.is_connected():
            await ctx.voice_client.disconnect()
        else:
            await ctx.send("I am not connected in any voice channel!")
    
    @commands.command(name='play')
    async def play(self, ctx,*, url : str):
        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.client.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
            await ctx.send('Now playing {}'.format(player.title))

        
    @commands.command(name='pause')
    async def pause(self, ctx):
        vc = ctx.voice_client
        if vc.is_playing():
            await ctx.voice_client.pause()
            await ctx.send("Paused")
        else:
            await ctx.send("I am not playing anything!")
    
    @commands.command(name='resume')
    async def resume(self, ctx):
        vc = ctx.voice_client
        if vc.is_paused():
            await ctx.voice_client.resume()
        else:
            await ctx.send("There's no music!")
    
    @commands.command(name='stop')
    async def stop(self, ctx):
        vc = ctx.voice_client

        vc.stop()
    

def setup(client):
    client.add_cog(Music(client))