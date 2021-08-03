from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command(name='ping', help="Check latency.")
    async def ping(self, ctx):
        await ctx.send(f'pong!\n{round(self.bot.latency * 1000)}ms')


def setup(client):
    client.add_cog(Ping(client))
