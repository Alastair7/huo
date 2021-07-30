from discord.ext import commands

class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='clear')
    async def clear(self, ctx, amount):
        await ctx.channel.purge(limit = amount + 1)
    
    @clear.error
    async def clearError(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Bad arguments were introduced.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing required arguments.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permissions to use this command.")
        else:
            await ctx.send("Something went wrong.")

def setup(client):
    client.add_cog(Clear(client))