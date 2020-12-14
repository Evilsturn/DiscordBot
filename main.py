import discord
from discord.ext import commands
from datetime import datetime
from asyncio import sleep


botToken = open("botToken.txt", "r")
botToken = botToken.read()
client = commands.Bot(command_prefix="!bot ")


@client.event
async def on_ready():
    print("Bot has been deployed")


@client.command()
async def hello(ctx):
    await ctx.send("Hi!")


async def displayEmbed(ctx, title, desc, colour):
    await sleep(2)
    main_embed = discord.Embed(
        title=title,
        description=desc,
        colour=colour)
    await sleep(2)
    return main_embed


@client.command()
async def reminder(ctx, task, timings):
    user = ctx.author.mention
    remindTime = 0
    now = datetime.now().strftime("%H%M%S")
    hour = int(now[0:2])
    min = int(now[2:4])
    sec = int(now[4:6])
    localTime = (hour*3600)+(min*60)+sec

    title = "Your Reminder"
    description = task
    colour = discord.Colour.dark_orange()
    branch_embed = await displayEmbed(ctx, title, description, colour)
    while True:
        now = datetime.now().strftime("%H%M%S")
        hour = int(now[0:2])
        min = int(now[2:4])
        sec = int(now[4:6])
        currentTime = (hour*3600)+(min*60)+sec
        unit = timings[-1].lower()
        newtimings = int(timings[:-1])
        if unit == 's':
            remindTime = localTime + newtimings
        elif unit == 'm':
            remindTime = localTime + (newtimings*60)
        elif unit == 'h':
            remindTime = localTime + (newtimings*3600)

        if currentTime == remindTime:
            await ctx.send(user)
            await ctx.send(embed=branch_embed)
            break


client.run(botToken)
