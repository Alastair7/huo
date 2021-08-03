from discord.ext import commands
import discord

class Bot_info(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='binfo', help="Get bot info.")
    async def getBotInfo(self,ctx):
        date_format = "%d/%m/%Y"
        # get bot.user
        bot_user = ctx.bot.user

        botName = str(bot_user.name)
        botDescription = f"Hello! my name is Hue. I'm a multipurpose bot with a mission: Make your life easier in your discord server." 
        botBirthday = str(bot_user.created_at.strftime(date_format))
        botCreator = str(ctx.guild.owner)[:-5]
        botServers = len(ctx.bot.guilds)

        embed = discord.Embed(description= botDescription, color=0x2E8B57)
        embed.set_author(name=botName, icon_url=bot_user.avatar_url)
        embed.add_field(name="Birthday", value=botBirthday, inline=True)
        embed.add_field(name='Creator', value=botCreator, inline=True)
        embed.add_field(name=f"Living in", value=f"{botServers} servers", inline=True )
        # Get channel
        systemChannel = discord.utils.get(ctx.guild.channels, id=835107161608552470)
        await systemChannel.send(embed = embed)

def setup(client):
    client.add_cog(Bot_info(client))