from discord.ext import commands
import discord

class User_info(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.command(name='uinfo')
    async def getUserInfo(self, ctx):
        userMember = ctx.author

        #Get Author info
        userName = str(userMember.name)
        userAvatar = userMember.avatar_url
        userJoiningDate = userMember.joined_at.strftime("%d/%m/%y")
        # Get Roles
        userRoles = []
        for role in userMember.roles:
            if role.name != "@everyone":
                userRoles.append(role.mention)
                if 'None' in userRoles:
                    userRoles.remove('None')
            else:
                userRoles.append('None')
        
        roles =", ".join(userRoles)
        #Create Embed
        embed = discord.Embed(title= userName, description=f"This legend is here since: **{userJoiningDate}**")
        embed.set_thumbnail(url= userAvatar)
        embed.add_field(name="Roles", value=roles, inline=True)

        # Get System Channel
        systemChannel = ctx.guild.system_channel

        await systemChannel.send(embed = embed)



def setup(client):
    client.add_cog(User_info(client))
