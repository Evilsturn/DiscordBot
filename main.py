from discord import Embed
from discord.ext import commands
from datetime import datetime,time
from asyncio import sleep

#bruh....you not using client from discord module...what is the use of importing it????
#discord.ext is child of discord module so it already does all the work of discord module...
#so I removed it OwO

botToken = botToken
client = commands.Bot(command_prefix="!bot")


@client.event
async def on_ready():
    print("Bot has been deployed")

"""
Before you go through this....I have to tell you something.
Even though you sent me the token, the bot itself wasn't added to a server
So, I couldn't test/do stuff with it(for a long time)
Thanks to NekoBot....I did testing with it.....that's the power of nyaa~~~!!! OwO
The program doesn't work anyway :(
"""

@client.command()
async def hello(ctx):
    await ctx.send("Hi!")

@client.command(pass_context=True, case_insensitive=True, alias=['reminder','rem','remindme'])
@commands.bot_has_permissions(embed_links=True, attach_files=True)
async def reminder(ctx, task, time):
    user=ctx.message.author
    embed_remainder=Embed(color=0xffffff,timestamp=datetime.now())#going for non-utc is good in this case OwO
    #change the color....I am bad at color concepts. This will change text of embed ofc
    embed_remainder.set_footer(text='Type reminder_info to understand the command format')
    seconds = 0#will be used later to convert things to seconds
    #shit goes really bad if you use ctx.send.....embeds look much better OwO

    if task is None:#description is null....can change this to NaN maybe...
        embed_remainder.add_field(name='NameNotFoundError', value='You have not inputted the subject for your reminder.') 

    elif time.lower().endswith("s"):
        seconds=seconds
        counter=f"{seconds}+ **seconds** "
    
    elif time.lower().endswith("m"):
        seconds=seconds+int(60) 
        counter=f"{seconds//60}+ **minutes** "
    
    elif time.lower().endswith("h"):
        seconds=seconds+int(60*60)
        counter=f"{seconds//60//60}+ **hours** "
    
    elif seconds < 10:
        embed_remainder.add_field(name='ValueTooLow',value='The value that you have given is too low, please make it to where its more than 10 seconds')
    
    elif seconds > 86400:
        embed_remainder.add_field(name='ValueTooHigh', value='The value you have given is too high, please make it to where its limited to just a single day.')
    
    #I just found out about an operator known as //. I will change this with all the mess that I have created
    #So, what // does is just return not only the value, but it returns it in rounded off....The mess with round() that I created before, is now clear as sunshine now
      
    else:
        await ctx.send(f"Reminder set for {task}, for a period of {counter}.")
        await sleep(seconds)
        await ctx.send(f"{user}! This is an alarm for the reminder you asked about {counter} ago for/to {task}")
        #putting f before print quotes allows formatting. No need to use .format and {}
        #goodshit always comes at the end of the program :(
        

@client.command(pass_context=True,case_insensitive=True)
@commands.bot_has_permissions(embed_links=True,attach_files=True) 
async def reminder_info(ctx):
    embed_info=Embed(title="You need to type in this format: !bot remainder {task} {time}h/m/s")
    embed_info.set_footer(text='For my sake...just put one unit(h or m or s) plz OwO')
    await ctx.send(embed=embed_info)

client.run(botToken)