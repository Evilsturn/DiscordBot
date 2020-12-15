from discord import Embed
from discord.ext import commands
from datetime import datetime, time
from asyncio import sleep


botToken = open("botToken.txt", "r")
botToken = botToken.read()
client = commands.Bot(command_prefix="!bot")


@client.event
async def on_ready():
    print("Bot has been deployed")


@client.command()
async def hello(ctx):
    await ctx.send("Hi!")


client.run(botToken)
