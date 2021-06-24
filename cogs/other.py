import discord
from discord.ext import commands


class Other(commands.Cog):

	def __init__(self, client):
		self.client = client


	@commands.command()
	async def info(self, ctx):
		embed = discord.Embed(colour=discord.Colour.blue())
		embed.add_field(name="Hi, I'm a discord bot!", value=f'You can invite me to your server!')
		await ctx.channel.send(embed=embed)
		await ctx.message.delete()


	@commands.command(aliases=["say"])
	async def embed(self, ctx, title, *, arg):
		await ctx.message.delete()
		embed = discord.Embed(colour=discord.Colour.blurple())
		embed.add_field(name=f'{title}', value=f"{arg}", inline=False)
		embed.set_footer(text=f'Embed by {ctx.message.author.name}')
		await ctx.channel.send(embed=embed)


	@commands.command()
	async def serverinfo(self, ctx):
		await ctx.message.delete()
		embed = discord.Embed(
			title=f"{ctx.guild.name} Server Information",
			color=discord.Color.blue()
		)
		embed.set_thumbnail(url=ctx.guild.icon_url)
		embed.add_field(name="Owner", value=f"<@{ctx.guild.owner_id}>", inline=True)
		embed.add_field(name="Region", value=ctx.guild.region, inline=True)
		embed.add_field(name="Created on",
						value=ctx.guild.created_at.strftime("%d/%m/%Y"))
		embed.add_field(name="Member Count",
						value=ctx.guild.member_count, inline=True)
		embed.add_field(
			name="Boosts", value=ctx.guild.premium_subscription_count)
		await ctx.send(embed=embed)


	@commands.command(aliases=["vote"])
	async def poll(self, ctx, *, message):
		await ctx.message.delete()
		embed = discord.Embed(colour=discord.Colour.blue())
		embed.add_field(name='React to this message to cast your vote!', value=f"{message}", inline=False)
		embed.set_footer(text=f'A poll by {ctx.message.author.name}')
		msg = await ctx.channel.send(embed=embed)
		await msg.add_reaction("<:greenyes:825673587293159425>")
		await msg.add_reaction("<:redno:825673832269479967>")


	@commands.command(aliases=['user_info', 'whois'])
	async def userinfo(self, ctx, member: discord.Member):
		embed = discord.Embed(
			colour=member.colour
		)
		embed.set_thumbnail(url=member.avatar_url)
		embed.set_author(name=f"User information {member}")
		embed.add_field(name="Joined at", value=member.joined_at.strftime(
			"%d/%m/%Y"), inline=True)
		embed.add_field(name="Account created at",
						value=member.created_at.strftime("%d/%m/%Y"), inline=True)
		embed.add_field(name="Top role",
						value=member.top_role.mention, inline=True)
		embed.add_field(name="Id", value=member.id, inline=True)
		embed.add_field(name="Nickname", value=member.nick, inline=True)
		embed.add_field(name="Bot?", value=member.bot, inline=True)
		embed.set_footer(text=f"Requested by |{ctx.message.author}|")
		await ctx.channel.send(embed=embed)
		await ctx.message.delete()


	@commands.command()
	async def ping(self, ctx):
		await ctx.message.delete()
		await ctx.send(f'Pong! `{round(self.client.latency * 1000)}ms`')

def setup(client):
	client.add_cog(Other(client))
