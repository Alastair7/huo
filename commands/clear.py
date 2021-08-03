from discord.ext import commands
import discord

class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='clear', help="Clear messages with a specific amount.")
    async def clear(self, ctx, amount):
        await ctx.channel.purge(limit = amount + 1)
        embed = discord.Embed(description=f"{amount + 1} messages were cleared.")
        await ctx.send(embed = embed)
    

def setup(client):
    client.add_cog(Clear(client))