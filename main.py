#Neko is love OwO
import discord
from discord import client
from discord.ext import commands

botToken = botToken
client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print("The bot has been deployed")


@client.command()
async def hello(ctx):
    await ctx.send("Hi!")

client.run(botToken)
