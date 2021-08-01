import discord
from discord.ext import commands
import youtube_dl
import traceback

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='join')
    async def join(self, ctx):
        if ctx.author.voice is None:
            ctx.send("You must be in a voice channel.")
        
        voiceChannel = ctx.author.voice.channel

        if ctx.voice_client is None:
            await voiceChannel.connect()
        else:
            await ctx.voice_client.move_to(voiceChannel)
    
    @commands.command(name='disconnect')
    async def disconnect(self,ctx):
        await ctx.voice_client.disconnect()
    
    @commands.command(name='play')
    async def play(self, ctx, url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect-delay_max 5', 'options': '-vn'}
        YOL_OPTIONS = {'format':"bestaudio"}

        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YOL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download = False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)

            vc.play(source)
        
    @commands.command(name='pause')
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send('Paused')
    
    @commands.command(name='resume')
    async def resume(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send('Resume')
def setup(client):
    client.add_cog(Music(client))