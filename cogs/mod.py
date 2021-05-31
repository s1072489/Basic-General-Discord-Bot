import discord
from discord.ext import commands


class Mod(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, user: discord.Member, *, reason):
		await ctx.message.delete()
		try:
			embed = discord.Embed(colour=discord.Colour.red())
			embed.set_author(name=f"Kicked")
			embed.add_field(name=f"You were kicked from {ctx.message.server.name} by {ctx.message.author.name} for {reason}", value="You can still join back with another invite", inline=False)
			user.send(embed=embed)
		except:
			pass
		try:
			await ctx.guild.kick(reason= f"{ctx.message.author.name} : {reason}")
			embed = discord.Embed(colour=discord.Colour.green())
			embed.set_author(name="Kick member")
			embed.add_field(name=f"{user} has been successfully kicked from this server", value="They can still join back with another invite")
			embed.set_footer(text=f'{user} was kicked by {ctx.message.author.name} for {reason}')
			await ctx.channel.send(embed=embed)
		except:
			embed = discord.Embed(colour=discord.Colour.red())
			embed.set_author(name="Kick member")
			embed.add_field(name=f'{user} was not able to be kicked from this server', value="This is most likely because Gigabyte's top role is the same or is lower than the target.")
			embed.set_footer(text=f'{user} was unsuccessfully kicked by {ctx.message.author.name} for {reason}')
			await ctx.channel.send(embed=embed, delete_after=5)


	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, user: discord.Member, *, reason):
		await ctx.message.delete()
		try:
			embed = discord.Embed(colour=discord.Colour.red())
			embed.set_author(name=f"Banned")
			embed.add_field(name=f"You were banned from {ctx.message.server.name} by {ctx.message.author.name} for {reason}", value="You can no longer join back with another invite", inline=False)
			user.send(embed=embed)
		except:
			pass

		try:
			await ctx.guild.ban(user=user, reason= f"{ctx.message.author.name} : {reason}")
			embed = discord.Embed(
				colour=discord.Colour.green()
			)
			embed.set_author(name='Ban member')
			embed.add_field(name=f'{user} has been successfully banned from this server', value='They cannot join back with another invite, unless they are unbanned')
			embed.set_footer(text=f'{user} was banned by {ctx.message.author.name}')
			await ctx.channel.send(embed=embed)
		except:
			embed = discord.Embed(colour=discord.Colour.red())
			embed.set_author(name="Ban member")
			embed.add_field(name=f'{user} was not able to be banned from this server', value="This is most likely because Gigabyte's top role is the same or is lower than the target.")
			embed.set_footer(text=f'{user} was unsuccessfully banned by {ctx.message.author.name} for {reason}')
			await ctx.channel.send(embed=embed, delete_after=5)


	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def unban(self, ctx, *, member):
		await ctx.message.delete()
		banned_users = await ctx.guild.bans()
		member_name, member_discriminator = member.split('#')
		for ban_entry in banned_users:
			user = ban_entry.user
		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			embed = discord.Embed(colour=discord.Colour.green())
			embed.set_author(name='Unban member')
			embed.add_field(name=f'{user} has been successfully unbanned from this server', value='They can now join back with an invite')
			embed.set_footer(text=f'{user} was unbanned by {ctx.message.author.name}')
			await ctx.channel.send(embed=embed, delete_after=5)


	@commands.command(aliases=['clear', 'delete'])
	@commands.has_permissions(manage_messages=True)
	async def purge(self, ctx, amount=0):
		await ctx.message.delete()
		await ctx.channel.purge(limit=amount+1)
		embed = discord.Embed(colour=discord.Colour.green())
		embed.set_author(name='Purge messages')
		embed.add_field(name=f'{amount} messages have been successfully deleted', value='No way of getting them back now')
		embed.set_footer(text=f'{amount} messages deleted by {ctx.message.author.name}')
		await ctx.channel.send(embed=embed, delete_after=5)


	@commands.command(aliases=['make_role'])
	@commands.has_permissions(manage_roles=True)
	async def create_role(self, ctx, *, name):
		await ctx.message.delete()
		guild = ctx.guild
		await guild.create_role(name=name)
		await ctx.send(f'Role `{name}` has been created',  delete_after=5)


	@commands.command(aliases=['give_role'])
	@commands.has_permissions(manage_roles=True)
	async def add_role(self, ctx, user: discord.Member, *, role: discord.Role):
		await ctx.message.delete()
		try:
			await user.add_roles(role)
			embed = discord.embed(colour=discord.Colour.green())
			embed.add_field(name=f"Role `{role}` has been added to {user.mention}", value=f"Role '{role}' added by {ctx.message.author.name}")
			await ctx.send(embed=embed)
		except:
			embed = discord.embed(colour=discord.Colour.red())
			embed.add_field(name=f"Role `{role}` was unable to be added to {user.mention}", value=f"This may be because thia role does not exist, or I do not have the permissions to add it.")
			await ctx.send(embed=embed, delete_after=5)


	@commands.command(aliases=['take_role'])
	@commands.has_permissions(manage_roles=True)
	async def remove_role(self, ctx, user: discord.Member, *, role: discord.Role):
		await ctx.message.delete()
		try:
			await user.remove_roles(role)
			embed = discord.embed(colour=discord.Colour.green())
			embed.add_field(name=f"Role `{role}` has been removed from {user.mention}", value=f"Role '{role}' removed by {ctx.message.author.name}")
			await ctx.send(embed=embed)
		except:
			embed = discord.embed(colour=discord.Colour.red())
			embed.add_field(name=f"Role `{role}` was unable to be removed from {user.mention}", value=f"This may be because thia role does not exist, or I do not have the permissions to remove it.")
			await ctx.send(embed=embed, delete_after=5)

	@commands.command()
	@commands.guild_only()
	@commands.has_permissions(manage_nicknames=True)
	async def nick(self, ctx, member: discord.Member, *, name: str = None):
		await member.edit(nick=name)
		message = f"Changed **{member.name}'s** nickname to **{name}**"
		if name is None:
			message = f"Reset `{member.name}'s` nickname"
		await ctx.send(message, delete_after=5)

def setup(client):
	client.add_cog(Mod(client))
