from discord.ext import commands
import discord

class Give_role(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='g_role')
    async def giveRoleToMember(self, ctx, member: discord.Member, memberRole: discord.Role):
        # get guild roles
        guildRoles = ctx.guild.roles

        # give member the role
        for role in guildRoles:
            roleToFind = role
            if roleToFind.name == memberRole.name:
                await member.add_roles(roleToFind)
                await ctx.send(f"{role.mention} role **added** to {member.mention}")
    
    @commands.command(name='r_role')
    async def removeRoleToMember(self, ctx, member: discord.Member, memberRole: discord.Role):
        # get guild roles
        guildRoles = ctx.guild.roles

        # remove membe the role
        for role in guildRoles:
            roleToRemove = role
            # find Role
            if(roleToRemove.name == memberRole.name):
                await member.remove_roles(roleToRemove)
                await ctx.send(f"{role.mention} role **removed** to {member.mention}")
    
    # ERROR HANDLING
    @giveRoleToMember.error
    async def giveRoleToMemberError(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"Bad arguments were introduced.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Missing required args.")
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send(f"Hey, expected`-g_role @(Someone) @(Some role)`")
        elif isinstance(error, commands.MemberNotFound) or isinstance(error, commands.RoleNotFound):
            await ctx.send(f"Member or role doesn't exist.")
        else:
            await ctx.send(f"Oops! something went wrong")

    @removeRoleToMember.error
    async def removeRoleToMemberError(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"Bad arguments were introduced.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Missing required args.")
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send(f"Hey, expected`-g_role @(Someone) @(Some role)`")
        elif isinstance(error, commands.MemberNotFound) or isinstance(error, commands.RoleNotFound):
            await ctx.send(f"Member or role doesn't exist.")
        else:
            await ctx.send(f"Oops! something went wrong")




def setup(client):
    client.add_cog(Give_role(client))