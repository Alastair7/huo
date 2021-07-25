from discord.ext import commands
import discord

class Welcome(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_member_join(self, member):

        # Get channel
        systemChannel = discord.utils.get(member.guild.channels, id=835107161608552470)
        # Get role
        miembroRole = discord.utils.get(member.guild.roles, id=868768097383890984)
        
        # Creating Embed
        embed = discord.Embed(title="Embed Added",description="Embed Description",color = 0xFF5733)
        embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
        embed.add_field(name="Field 1", value="This is field 1", inline = False)
        embed.add_field(name="Field 2", value="This is field 2", inline = True)
        embed.add_field(name= "Field 3", value="This is field 3", inline= True)
        embed.set_thumbnail(url = member.avatar_url)
        embed.set_footer(text="This is the footer.")
        #Send Embed
        if systemChannel is not None:
            # Give new member 'Miembro' role
            await member.add_roles(miembroRole)
            await systemChannel.send(embed = embed)
    
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        # Get channel
        systemChannel = discord.utils.get(member.guild.channels, id=835107161608552470)

        # Creating Embed
        embed = discord.Embed(title="Embed Removed",description="Embed Description",color = 0xFF5733)
        embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
        embed.add_field(name="Field 1", value="This is field 1", inline = False)
        embed.add_field(name="Field 2", value="This is field 2", inline = True)
        embed.add_field(name= "Field 3", value="This is field 3", inline= True)
        embed.set_thumbnail(url = member.avatar_url)
        embed.set_footer(text="This is the footer.")

        #Send Embed
        if systemChannel is not None:
            await systemChannel.send(embed = embed)


def setup(client):
    client.add_cog(Welcome(client))