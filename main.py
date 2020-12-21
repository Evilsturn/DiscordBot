import discord
from discord.ext import commands
from asyncio import sleep
import os
import random

botToken = open("botToken.txt", "r")
botToken = botToken.read()
client = commands.Bot(command_prefix="!bot ")

@client.event
async def on_ready():
    print("Mother file is online")

@client.event
async def on_member_join(member):
    await member.create_dm()
    choice=random.randrange(1,3)
    if choice==1:
        await member.dm_channel.send(f'Hello! {member.name}, welcome to my Discord server!')
    if choice==2:
        await member.dm_channel.send(f"Hope you have a great time in our server")
    if choice==3:
        await member.dm_channel.send(f"WELCOME~~~~ {member.name}, this is a bot message to welcome you!")

async def displayEmbed(ctx,title,desc,colour):
    await sleep(2)
    main_embed = discord.Embed(
        title=title,
        description=desc,
        colour=colour)
    await sleep(2)
    return main_embed

for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(botToken)
