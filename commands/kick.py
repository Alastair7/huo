from discord.ext import commands
import discord

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

def setup(client):
    client.add_cog(Kick(client))