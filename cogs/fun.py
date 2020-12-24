import discord
from discord.ext import commands
from main import displayEmbed
import wikipedia as wiki
import random
from mal.anime_search import AnimeSearch
from mal.manga_search import MangaSearch
from asyncio import sleep

class Fun(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print("Fun cog is online")

	@commands.command(pass_context = True)
	async def search(self, ctx, query):
		try:
			user = ctx.author.mention
			title = query.upper()
			desc = wiki.summary(query, sentences=5, chars=0, auto_suggest=False, redirect=True)
			color = 0xff0059
			branch_embed = await displayEmbed(ctx,title,desc,color)
			branch_embed.set_thumbnail(url="{0}".format("https://cdn.discordapp.com/attachments/726777454009778187/790528898575106058/1200px-Wikipedia-logo-v2.png"))
			await ctx.send(user)
			await ctx.send(embed = branch_embed)
			
		except wiki.DisambiguationError as e:
			await ctx.send(e)

	@commands.command(aliases=['8ball'])
	async def eightball(self,ctx,string):
		decision=random.randrange(0,2)
		desc=f"Question asked: {string}"
		color=0x000000
		if(decision==0):
			title="**NO!!!**"
			no_embed=await displayEmbed(ctx,title,desc,color)
			await ctx.send(embed=no_embed)
		elif(decision==1):
			title="**YES!!!**"
			yes_embed=await displayEmbed(ctx,title,desc,color)
			await ctx.send(embed=yes_embed)
 
	@commands.command()
	async def animesearch(self,ctx,name):
		user_mention=ctx.author.mention
		search=AnimeSearch(name,timeout=30)
		color=0x000000
		try:
			
			firstHit=search.results[0].title
			synopsis=search.results[0].synopsis
			episodes=search.results[0].episodes
			score=search.results[0].score
			img_url=search.results[0].image_url
			url=search.results[0].url
			anime_embed=await displayEmbed(ctx,firstHit,synopsis,color)
			anime_embed.add_field(name="Number of episodes:",value=episodes,inline=True)
			anime_embed.add_field(name="Score:",value=score,inline=True)
			anime_embed.set_thumbnail(url=img_url)
			anime_embed.set_footer(text=url)
				
			await ctx.send(user_mention)
			await ctx.send(embed=anime_embed)
		except TimeoutError:
			await ctx.send(user_mention)
			await ctx.send("Try to reply within 30 seconds")

	@commands.command()
	async def mangasearch(self,ctx,name):
		user_mention=ctx.author.mention
		search=MangaSearch(name,timeout=30)
		color=0xffffff
		try:

		    firstHit=search.results[0].title
		    synopsis=search.results[0].synopsis
		    volumes=search.results[0].volumes
		    score=search.results[0].score
		    img_url=search.results[0].image_url
		    url=search.results[0].url
		    manga_embed=await displayEmbed(ctx,firstHit,synopsis,color)
		    manga_embed.add_field(name="Number of volumes:",value=volumes,inline=True)
		    manga_embed.add_field(name="Score:",value=score,inline=True)
		    manga_embed.set_thumbnail(url=img_url)
		    manga_embed.set_footer(text=url)
		    
		    await ctx.send(user_mention)
		    await ctx.send(embed=manga_embed)
		except TimeoutError:
			await ctx.send(user_mention)
			await ctx.send("Try to reply within 30 seconds")

	@commands.command(pass_context=True, aliases=["roulette","russianroulette","rr"])
	async def russian_roulette(self,ctx,rounds):
		member=ctx.author
		if(int(rounds)>6):
			await ctx.send("A magnum has 6 capacity....how many bullets are you gonna put?")
			await ctx.send("Min:0, Max:6")
		elif int(rounds) == 0:
			await ctx.send("No load detected.....")
			await ctx.send("Min:0, Max:6")
		elif int(rounds)<0:
			ctx.send("No u")
			
		chamber=random.randrange(int(rounds),7)
		if(int(rounds)>0 and int(rounds)<=6):
		
			if(chamber==6):
				await ctx.send("Rolling the barrel")
				await ctx.send("Ah~ It seems like ........oh fu---")
				await sleep(1)
				await ctx.send("**BANG**")
				await member.create_dm()
				await member.dm_channel.send("You died")
				await sleep(2)
				await ctx.guild.kick(user=member, reason="Got shot by a .457 magnum")

			else:
				await ctx.send("Rolling the barrel")
				await ctx.send("Ah~ It seems like ........oh fu---")
				await sleep(1)
				await ctx.send("**CHING**")
				await sleep(2)
				await ctx.send("You survived OwO")
	
	@russian_roulette.error
	async def russian_roulette_error(self,ctx,error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("Load the chamber with at least a single bullet....or more")
			await ctx.send("Min:1, Max:6")
def setup(client):
	client.add_cog(Fun(client))