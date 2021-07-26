from asyncio.windows_events import NULL
from discord import activity
from discord.activity import CustomActivity
from discord.ext import commands
import discord

class User_info(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.command(name='uinfo')
    async def getUserInfo(self, ctx, member: discord.Member):
        authorMember = member

        #Get Author info
        authorName = str(authorMember.name)
        authorAvatar = authorMember.avatar_url
        authorJoiningDate = authorMember.joined_at.strftime("%d/%m/%y")
        authorRoles = []

        for role in authorMember.roles:
            if role.name != "@everyone":
                authorRoles.append(role.name)
            else:
                authorRoles.append('None')
        
        roles =", ".join(authorRoles)
        #Create Embed
        embed = discord.Embed(title= authorName, description=f"This legend is here since: **{authorJoiningDate}**")
        embed.set_thumbnail(url= authorAvatar)
        embed.add_field(name="Roles", value=roles, inline=True)
        systemChannel = ctx.guild.system_channel

        await systemChannel.send(embed = embed)



def setup(client):
    client.add_cog(User_info(client))
