from discord.ext import commands
import discord

class Give_role(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='g_role', help="Give an existent role to a member.")
    async def giveRoleToMember(self, ctx, member: discord.Member, memberRole: discord.Role):
        # get guild roles
        guildRoles = ctx.guild.roles

        # give member the role
        for role in guildRoles:
            roleToFind = role
            if roleToFind.name == memberRole.name:
                await member.add_roles(roleToFind)
                embed = discord.Embed(description=f"{role.mention} role **added** to {member.mention}")
                await ctx.send(embed = embed)
    
    @commands.command(name='r_role', help="Remove an existent role to a member.")
    async def removeRoleToMember(self, ctx, member: discord.Member, memberRole: discord.Role):
        # get guild roles
        guildRoles = ctx.guild.roles

        # remove membe the role
        for role in guildRoles:
            roleToRemove = role
            # find Role
            if(roleToRemove.name == memberRole.name):
                await member.remove_roles(roleToRemove)
                embed = discord.Embed(description=f"{role.mention} role **removed** to {member.mention}")
                await ctx.send(embed = embed)
    




def setup(client):
    client.add_cog(Give_role(client))