import json
import discord
from discord.ext import commands

# Getting config.json data
with open('config.json') as input_file:
    data = json.load(input_file)

# Setting up bot data
token = data["TOKEN"]   
prefix = data["PREFIX"]
name = data["BOT_NAME"]

client = commands.Bot(command_prefix=prefix)

# COGS
initial_extensions = ['commands.example']

# LOAD COGS
if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)


@client.event
async def on_ready():
    print('Logged in as {}'.format(name))

client.run(token)