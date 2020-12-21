import discord
from discord.ext import commands
from main import displayEmbed
import wikipedia as wiki
import random
from mal.anime_search import AnimeSearch

class Fun(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print("fun cog is online")

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
				
				await ctx.send(embed=anime_embed)
			except TimeoutError:
				await ctx.send(ctx.author.mention)
				await ctx.send("Try to reply within 30 seconds")

def setup(client):
	client.add_cog(Fun(client))