import json
import os
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
    for filename in os.listdir(f"./commands"):
        if filename.endswith(f".py"):
            client.load_extension(f"commands.{filename[:-3]}")
            print(f"Command {filename[:-3]} loaded")


@client.event
async def on_ready():
    print('Logged in as {}'.format(name))

client.run(token)