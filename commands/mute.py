from discord.ext import commands
import discord
from discord.ext.commands.errors import MemberNotFound

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
    
    @muteUser.error
    async def muteUserError(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the permissions to use this command.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Bad arguments were introduced.")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("Member not found")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing required arguments.")
    
    @unMuteUser.error
    async def unMuteUserError(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the permissions to use this command.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Bad arguments were introduced.")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("Member not found")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing required arguments.")

def setup(client):
    client.add_cog(Mute(client))