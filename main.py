import discord
from discord.ext import commands
from datetime import datetime
from asyncio import sleep
from random import randrange


botToken = open("botToken.txt", "r")
botToken = botToken.read()
client = commands.Bot(command_prefix="!bot ")


@client.event
async def on_ready():
    print("Bot has been deployed")


@client.command()
async def hello(ctx):
    await ctx.send("Hi!")

async def displayEmbed(ctx,title,colour):
    await sleep(2)
    main_embed = discord.Embed(
        title=title,
        colour=colour)
    await sleep(2)
    return main_embed


@client.command()
async def reminder(ctx, task, timings):
    user_mention = ctx.author.mention
    user_name=ctx.author.display_name
    remindTime = 0
    now = datetime.now().strftime("%H%M%S")
    hour = int(now[0:2])
    min = int(now[2:4])
    sec = int(now[4:6])
    localTime = (hour*3600)+(min*60)+sec

    image_link=["https://cdn.animenewsnetwork.com/thumbnails/max500x500/cms/interest/75566/323bced8.jpg",
                "https://cdn.animenewsnetwork.com/thumbnails/max500x500/cms/interest/75566/a34661be.jpg",
                "https://cdn.animenewsnetwork.com/thumbnails/max500x500/cms/interest/75566/1192947e.jpg",
                "https://cdn.animenewsnetwork.com/thumbnails/max500x500/cms/interest/75566/a57fd2dc.jpg",
                "https://cdn.animenewsnetwork.com/thumbnails/max500x500/cms/interest/75566/c6fc8a3e.jpg"]
    image_length=len(image_link)-1
    footer_text=[" ...Heh. You're making the face of someone who's not awake yet. I want you to wake up soon, though. Is that OK?...",
                 "...Hey. Hey! Wake up! How many times do you think I've tried to get you up!? WAKE. UP. NOW!..",
                 "Hey, hey! Wake up, wake up~! We have plans to burn the world today, right? If you don't wake up, it's boring for me~~~!.",
                 "...Geez, you really are bad at waking up. You make me wake you up every time.. Honestly...xD",
                 "Hahahah....I have waked you up now!~~~ Now just go and do the work!!!! [so that you don't get punished like me]......huh? that was nothing! GO. TO. WORK."]
    footer_length=len(footer_text)-1

    title = "REMINDER!!!!"
    colour = discord.Colour.dark_red()
    branch_embed = await displayEmbed(ctx,title,colour)
    branch_embed.set_author(name=user_name,icon_url=ctx.author.avatar_url)
    branch_embed.set_thumbnail(url="{0}".format(image_link[randrange(0, image_length)]))
    branch_embed.add_field(name="**Information:**", value="**Reminder set to: **" +str(task),inline=False)
    branch_embed.set_footer(text="{0}".format(footer_text[randrange(0, footer_length)]))
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
            await ctx.send(user_mention)
            await ctx.send(embed=branch_embed)
            break

@client.command(pass_context=True)
async def reminder_info(ctx):
    title="How to reminder 101!"
    colour=discord.Colour.green()
    info_embed=await displayEmbed(ctx, title, colour)
    info_embed.add_field(name="Format:",value="`------------------`",inline=False)
    info_embed.add_field(name='!bot reminder "your task" time in s/m/h ',value="`------------------`",inline=False)

    await ctx.send(embed=info_embed)

client.run(botToken)
