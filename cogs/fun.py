import discord
from discord.ext import commands
from main import displayEmbed
import wikipedia as wiki

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

def setup(client):
	client.add_cog(Fun(client))

