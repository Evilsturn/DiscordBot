import discord
from discord.ext import commands
from asyncio import sleep
import os
import random

botToken = open("botToken.txt", "r")
botToken = botToken.read()
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=["!bot ","!bot","!BOT ","!BOT"],intents=intents,case_insensitive=True)

@client.event
async def on_ready():
    print("Mother file is online")

@client.event
async def on_member_join(member):
    await member.create_dm()
    choice=random.randrange(1,3)
    if choice==1:
        await member.dm_channel.send(f'Hello! {member.name}, welcome to my Discord server!')
    elif choice==2:
        await member.dm_channel.send(f"Hope you have a great time in our server")
    elif choice==3:
        await member.dm_channel.send(f"WELCOME~~~~ {member.name}, this is a bot message to welcome you!")
    channel=client.get_channel(648197664659341394)
    await channel.edit(name=f'Member Count: {channel.guild.member_count}')

@client.event
async def on_member_remove(member):
    channel=client.get_channel(648197664659341394)
    await channel.edit(name=f'Member Count: {channel.guild.member_count}')

async def displayEmbed(ctx,title,desc,colour):
    main_embed = discord.Embed(
        title=title,
        description=desc,
        colour=colour)
    return main_embed

@client.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(ctx.author.mention)
        await ctx.send("Such command does not exist, type '!bot help'")

for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(botToken)