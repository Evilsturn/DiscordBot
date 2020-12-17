import discord
from discord.ext import commands

class Moderation(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(pass_context=True)
	async def ban(ctx,members:discord.Member,reason=None):
	    await ctx.guild.ban(user=members, reason=reason)
	    channel= self.client.get_channel(648197664659341394)
	    ban_embed=await displayEmbed(ctx, title=f"User{members} has been banned by {ctx.author.name}",colour=discord.Colour.dark_gold())
	    await channel.send(embed=ban_embed)

	@commands.command(pass_context=True)
	async def kick(ctx, members:discord.Member, reason=None):
	    await ctx.guild.kick(user=members, reason=reason)
	    channel= self.client.get_channel(648197664659341394)
	    kick_embed=await displayEmbed(ctx, title=f"User{members} has been kicked by {ctx.author.name}",colour=discord.Colour.dark_gold())
	    await ctx.channel.send(embed=kick_embed)

	@commands.command(pass_context=True)
	async def clear(self,ctx, delete=400):
	    await ctx.channel.purge(limit=delete+1)

def setup(client):
    	client.add_cog(Moderation(client))    
		