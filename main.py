import discord
from discord.ext import commands
from asyncio import sleep
import os

botToken = open("botToken.txt", "r")
botToken = botToken.read()
client = commands.Bot(command_prefix="!bot ")

@client.event
async def on_ready():
    print("Mother file is online")

@client.command()
async def hello(ctx):
    await ctx.send("Hi!")

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
