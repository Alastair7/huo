from discord.ext import commands
import discord
from discord.ext.commands.errors import MemberNotFound

class Mute(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='mute', help="Mute a member from the server.")
    async def muteUser(self, ctx, member: discord.Member,*, reason = None):
        muteRole = discord.utils.get(member.guild.roles, id=869894243022438400) 
        if reason is None:
            embed = discord.Embed(description=f'{member.name} was muted || **Reason:** {reason}')
            await ctx.send(embed = embed)
            await member.add_roles(muteRole) 
        else:
            embed = discord.Embed(description=f'{member.name} was muted || **Reason:** {reason}')
            await member.add_roles(muteRole)
            await ctx.send(embed = embed)
    
    @commands.command(name='unmute', help="Unmute a member from the server.")
    async def unMuteUser(self, ctx, member: discord.Member):
        embed = discord.Embed(description=f'{member.name} was unmuted')
        muteRole = discord.utils.get(member.guild.roles, id=869894243022438400) 
        await member.remove_roles(muteRole)
        await ctx.send(embed = embed)
    


def setup(client):
    client.add_cog(Mute(client))