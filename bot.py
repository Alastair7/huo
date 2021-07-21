import json
import discord

# Getting config.json data
with open('config.json') as input_file:
    data = json.load(input_file)

# Setting up bot data
token = data["TOKEN"]   
prefix = data["PREFIX"]
name = data["BOT_NAME"]

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {}'.format(name))

# TO-DO: IMPLEMENT COGS LOADER

client.run(token)