from discord.ext import commands

class example(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send(f'pong!\n{round(self.bot.latency * 1000)}ms')


def setup(bot):
    bot.add_cog(example(bot))
