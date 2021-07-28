from discord.ext import commands
import discord

class Mute(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='mute')
    async def muteUser(self, ctx, member: discord.Member,*, reason = None):
        muteRole = discord.utils.get(member.guild.roles, id=869894243022438400) 
        if reason is None:
            print(f'{member.name} muted || **Reason:** {reason}')
            await member.add_roles(muteRole) 
        else:
            await member.add_roles(muteRole)
            print(f'{member.name} muted || **Reason:** {reason}')
    
    @commands.command(name='unmute')
    async def unMuteUser(self, ctx, member: discord.Member):
        muteRole = discord.utils.get(member.guild.roles, id=869894243022438400) 
        await member.remove_roles(muteRole)
        print(f'{member.name} unmuted')

def setup(client):
    client.add_cog(Mute(client))