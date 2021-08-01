from discord.ext import commands
import traceback

class Error_handler(commands.Cog):
    def __init__(self, client):
        self.client = client
    

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"You don't have the permission to use this command.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send(f"Bad arguments were introduced.")
        elif isinstance(error, commands.MemberNotFound ):
            await ctx.send(f"Couldn't find member.")
        elif isinstance(error, commands.RoleNotFound):
            await ctx.send(f"Couldn't find role.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Required arguments are missing.")
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send(f"This command doesn't exists")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"This command is on cooldown.")
        else:
            traceback.print_exc()
    
def setup(client):
    client.add_cog(Error_handler(client))
