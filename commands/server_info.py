from discord.ext import commands
import discord

class Server_info(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='sinfo')
    async def getServerInfo(self, ctx):
        date_format = "%d/%m/%Y" 
        # Get server information
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)
        owner = str(ctx.guild.owner)
        region = str(ctx.guild.region).capitalize()
        members = str(ctx.guild.member_count)
        # Create Embed
        embed = discord.Embed(description = description, color=0x2E8B57)
        embed.add_field(name='Owner', value=owner[:-5], inline=True)
        embed.add_field(name='Region', value=region, inline=True)
        embed.add_field(name='Members', value=members, inline=True)
        embed.add_field(name='Birthday', value=str(ctx.guild.created_at.strftime(date_format)), inline=True)
        embed.set_author(name=name, icon_url=ctx.guild.icon_url)
        # Get channel
        systemChannel = discord.utils.get(ctx.guild.channels, id=835107161608552470)
        await systemChannel.send(embed = embed)

def setup(client):
    client.add_cog(Server_info(client))