import json
import os
from discord.ext import commands
import discord
from discord.ext.commands.errors import ExtensionNotFound


# Getting config.json data
with open('config.json') as input_file:
    data = json.load(input_file)

# Setting up bot data
token = data["TOKEN"]   
prefix = data["PREFIX"]
name = data["BOT_NAME"]

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=prefix, intents = intents)



# COGS

#LOAD SPECIFIC COG
@client.command()
async def load(ctx,extension):
    client.load_extension(f'commands.{extension}')
    try:
        print(f'Command: {extension} --> LOADED')
    except ExtensionNotFound:
        print(f'Command: {extension} --> UNLOADED')

#UNLOAD SPECIFIC COG
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'commands.{extension}')
    print(f'Command: {extension} --> UNLOADED')

#RELOAD SPECIFIC COG
@client.command()
async def reload(ctx, extension):
    client.reload_extension(f'commands.{extension}')
    try:
        print(f'Command: {extension} --> RELOADED')
    except ExtensionNotFound:
        print(f'Command: {extension} --> UNLOADED')

# LOAD COGS
if __name__ == '__main__':
    for filename in os.listdir(f"./commands"):
        if filename.endswith(f".py"):
            client.load_extension(f"commands.{filename[:-3]}")
            try:
                print(f"Command: {filename[:-3].capitalize()} --> LOADED")
            except ExtensionNotFound:
                print(f"Command: {filename[:-3].capitalize()} --> UNLOADED")
                



@client.event
async def on_ready():
    print('Logged in as {}'.format(name))

client.run(token)