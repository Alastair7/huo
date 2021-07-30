from discord.ext import commands
import discord

class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='ban')
    async def banUser(self, ctx, user: discord.Member,*, reason = None):
        if reason is None:
            await ctx.send(f"{user.mention} was **banned** || Reason: None")
            await user.ban()
        else:
            await ctx.send(f"{user.mention} was **banned** || Reason: {reason}")
            await user.ban(reason=reason)
    
    @commands.command(name='unban')
    async def unBanUser(self, ctx, member:discord.User):
        # Get banned people from this guild
        usersBanned = await ctx.guild.bans()

        for userInList in usersBanned:
            userBanned = userInList.user # Get user object from the list
            if (userBanned.name, userBanned.discriminator) == (member.name, member.discriminator):
                await ctx.guild.unban(userBanned)
                await ctx.send(f"{userBanned.mention} was **unbanned**")
            else:
                await ctx.send("User not found")
            
    @banUser.error
    async def banUserError(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Bad arguments were introduced.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f"You don't have permissions to use this command.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Missing required arguments.")
    
    @unBanUser.error
    async def unBanUserError(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Bad arguments were introduced.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f"You don't have permissions to use this command.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Missing required arguments.")
            


def setup(client):
    client.add_cog(Ban(client))