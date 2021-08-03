from discord.ext import commands
import discord

class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='ban',help = "Ban a member from the server. Reason is optional")
    async def banUser(self, ctx, user: discord.Member,*, reason = None):
        if reason is None:
            embed = discord.Embed(description=f"{user.mention} was **banned** || Reason: None")
            await ctx.send(embed = embed)
            await user.ban()
        else:
            embed = discord.Embed(description=f"{user.mention} was **banned** || Reason: {reason}")
            await ctx.send(embed = embed)
            await user.ban(reason=reason)
    
    @commands.command(name='unban', help="Unban a member from the server. Reason is optional")
    async def unBanUser(self, ctx, member:discord.User):
        # Get banned people from this guild
        usersBanned = await ctx.guild.bans()

        for userInList in usersBanned:
            userBanned = userInList.user # Get user object from the list
            if (userBanned.name, userBanned.discriminator) == (member.name, member.discriminator):
                await ctx.guild.unban(userBanned)
                embed = discord.Embed(description=f"{userBanned.mention} was **unbanned**")
                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(description = "User not found")
                await ctx.send(embed = embed)

            


def setup(client):
    client.add_cog(Ban(client))