from discord.ext import commands
import traceback
import discord

class Error_handler(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description="You don't have permissions to use this command.")
            await ctx.send(embed = embed)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(description="Bad arguments were introduced.")
            await ctx.send(embed = embed)
        elif isinstance(error, commands.MemberNotFound ):
            embed = discord.Embed(description="Couldn't find member.")
            await ctx.send(embed = embed)
        elif isinstance(error, commands.RoleNotFound):
            embed = discord.Embed(description="Couldn't find role.")
            await ctx.send(embed = embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description="Required arguments are missing.")
            await ctx.send(embed = embed)
        elif isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(description="Command not found.")
            await ctx.send(embed = embed)
        elif isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(description="This command is on cooldown")
            await ctx.send(embed = embed)
        else:
            traceback.print_exc()
    
def setup(client):
    client.add_cog(Error_handler(client))
