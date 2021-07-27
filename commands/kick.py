from discord.ext import commands
import discord

class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='kick')
    async def kickUser(self, ctx, user:discord.Member,*,reason = None):

        if reason is None:
            await ctx.send(f"{user.mention} was **kicked** || Reason: None")
            await user.kick()
        else:
            await ctx.send(f"{user.mention} was **kicked** || **Reason:** {reason}")
            await user.kick(reason=reason)

def setup(client):
    client.add_cog(Kick(client))