import discord
from discord import client
from discord.ext import commands

client = commands.Bot(command_prefix="!")


@client.event
async def on_login():
    print("The bot has been deployed")
