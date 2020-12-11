import discord
from discord.ext import commands
from datetime import datetime, time
# from asyncio import sleep


botToken = 'NzI5MjM3NzU0Mzk0OTY4MTA0.XwGBlQ.ZSEUzTqELtMNqnQPc7u4nYYbnhE'
client = commands.Bot(command_prefix="!bot ")


@client.event
async def on_ready():
    print("Bot has been deployed")


@client.command()
async def hello(ctx):
    await ctx.send("Hi!")


#  Create a Method for eg displayEmbed(parameters)
#  Create a embed template so that we can call this method and pass in some information
#  and it will post an embed with the following information
#  OH yeah I did not mention it but can you make @ feature so that when recieving the Reminder the user gets notified
#  K thanks :D


@client.command()
async def reminder(ctx, task, timings):
    remindTime = 0
    now = datetime.now().strftime("%H%M%S")
    hour = int(now[0:2])
    min = int(now[2:4])
    sec = int(now[4:6])
    localTime = (hour*3600)+(min*60)+sec

    displayEmbed = discord.Embed(
        title="Your reminder",
        description=task,
        colour=discord.Colour.dark_orange(),
    )

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
            await ctx.send(embed=displayEmbed)
            break


client.run(botToken)
