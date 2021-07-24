from discord.colour import Color
from discord.ext import commands
import discord

class Welcome(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(member)
        systemChannel = discord.utils.get(member.guild.channels, id=835107161608552470)
        embed = discord.Embed(title="Embed Title",description="Embed Description",color = 0xFF5733)
        embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
        embed.add_field(name="Field 1", value="This is field 1", inline = False)
        embed.add_field(name="Field 2", value="This is field 2", inline = True)
        embed.add_field(name= "Field 3", value="This is field 3", inline= True)
        embed.set_thumbnail(url = member.avatar_url)
        embed.set_footer(text="This is the footer.")
        if systemChannel is not None:
            await systemChannel.send(embed = embed)

def setup(client):
    client.add_cog(Welcome(client))