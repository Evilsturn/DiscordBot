import discord
from discord.ext import commands
from main import displayEmbed

class Moderation(commands.Cog):
	def __init__(self, client):
		self.client = client	
	
	@commands.Cog.listener()
	async def on_ready(self):
		print("Moderation cog is online")

	@commands.command(pass_context=True)
	async def ban(self,ctx,members:discord.Member,reason=None):
	    await ctx.guild.ban(user=members, reason=reason)
	    channel= self.client.get_channel(648197664659341394)
	    ban_embed=await displayEmbed(ctx, title=f"User{members} has been banned by {ctx.author.name}",colour=discord.Colour.dark_gold())
	    await channel.send(embed=ban_embed)

	@commands.command(pass_context=True)
	async def kick(self,ctx, members:discord.Member, reason=None):
	    await ctx.guild.kick(user=members, reason=reason)
	    channel= self.client.get_channel(648197664659341394)
	    kick_embed=await displayEmbed(ctx, title=f"User{members} has been kicked by {ctx.author.name}",colour=discord.Colour.dark_gold())
	    await ctx.channel.send(embed=kick_embed)

	@commands.command(pass_context=True)
	async def clear(self,ctx, delete=0):
		if(delete==0):
			await ctx.channel.purge(limit=delete+1)
			title="No value or zero value"
			desc="Please put value more than 1"
			color=discord.Color.dark_red()
			clear_embed=await displayEmbed(ctx,title,desc,color)			
			await ctx.send(ctx.author.mention)
			await ctx.send(embed=clear_embed)
		else:
			await ctx.channel.purge(limit=delete+1)

def setup(client):
    client.add_cog(Moderation(client))    
		