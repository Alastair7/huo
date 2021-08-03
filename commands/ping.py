from discord.ext import commands
import discord

class Ping(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command(name='ping', help="Check latency.")
    async def ping(self, ctx):
        embed = discord.Embed(description=f"pong!\n{round(self.bot.latency * 1000)}ms")
        await ctx.send(embed = embed)


def setup(client):
    client.add_cog(Ping(client))
