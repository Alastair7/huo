from discord.ext import commands
import discord
from discord.ext.commands.errors import MissingPermissions

class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='kick', help="Kick a member from the server")
    async def kickUser(self, ctx, member:discord.Member,*,reason = None):

        if reason is None:
            embed = discord.Embed(description=f"{member.mention} was **kicked** || **Reason:** None")
            await ctx.send(embed = embed)
            await member.kick()
        else:
            embed = discord.Embed(description=f"{member.mention} was **kicked** || **Reason:** {reason}")
            await ctx.send(embed = embed)
            await member.kick(reason=reason)

def setup(client):
    client.add_cog(Kick(client))