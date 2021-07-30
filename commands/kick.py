from discord.ext import commands
import discord
from discord.ext.commands.errors import MissingPermissions

class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='kick')
    async def kickUser(self, ctx, member:discord.Member,*,reason = None):

        if reason is None:
            await ctx.send(f"{member.mention} was **kicked** || Reason: None")
            await member.kick()
        else:
            await ctx.send(f"{member.mention} was **kicked** || **Reason:** {reason}")
            await member.kick(reason=reason)

    @kickUser.error
    async def kickUserError(self,ctx,error):
        if isinstance(error,commands.BadArgument):
            await ctx.send(f"Bad arguments were introduced.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Missing required arguments.")
        elif isinstance(error, MissingPermissions):
            await ctx.send(f"Missing permissions.")
        else:
            await ctx.send(f"Oops! something went wrong.")
def setup(client):
    client.add_cog(Kick(client))