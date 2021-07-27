from discord.ext import commands
import discord

class Mute(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='mute')
    async def muteUser(self, ctx, user: discord.Member, *, reason: str):
        await user.edit(Mute = True, reason= reason)
        print(f'{user.name} muted')
    
    @commands.command(name='unmute')
    async def unMuteUser(self, ctx, user: discord.Member):
        await user.edit(Mute = False)
        print(f'{user.name} unmuted')

def setup(client):
    client.add_cog(Mute(client))