from discord.ext import commands
import discord
from discord.ext.commands.bot import Bot

class Bot_info(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='binfo')
    async def getBotInfo(self,ctx):
        date_format = "%d/%m/%Y"
        # get bot.user
        bot_user = ctx.bot.user

        botName = str(bot_user.name)
        botBirthday = str(bot_user.created_at)
        botCreator = str(ctx.guild.owner)[:-5]

        embed = discord.Embed(color=0x2E8B57)
        embed.set_author(name=botName, icon_url=bot_user.avatar_url)
        embed.add_field(name="Birthday", value=botBirthday, inline=True)
        embed.add_field(name='Creator', value=botCreator, inline=True)
        # Get channel
        systemChannel = discord.utils.get(ctx.guild.channels, id=835107161608552470)
        await systemChannel.send(embed = embed)

def setup(client):
    client.add_cog(Bot_info(client))