import discord
from discord.ext import commands


class Events(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print(f"Bot online and logged in as {self.client.user}")
		await self.client.change_presence(activity=discord.Game(f'+help in {len(self.client.guilds)} guilds'))

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		await ctx.message.delete()
		if isinstance(error, commands.CommandNotFound):
			embed = discord.Embed(colour=discord.Colour.red())
			embed.add_field(
				name='The following error occured while trying running this command',
				value='CommandNotFound', inline=False)
			embed.set_footer(text=f'Please try again | {ctx.message.author.name} | If you belive this is a error, please DM HelloWorld#7091')
			await ctx.channel.send(embed=embed, delete_after=10)

		elif isinstance(error, commands.MissingPermissions):
			embed = discord.Embed(colour=discord.Colour.red())
			embed.add_field(name='The following error occured while trying running this command',
							value='MissingRequiredPermissions', inline=False)
			embed.add_field(name='You do not have the required permission to use this command',
							value='For the required permissions of each command, use `+help`', inline=False)
			embed.set_footer(text=f'| {ctx.message.author.name} | If you belive this is a error, please DM HelloWorld#7091')
			await ctx.channel.send(embed=embed, delete_after=10)

		elif isinstance(error, commands.MissingRequiredArgument):
			embed = discord.Embed(colour=discord.Colour.red())
			embed.add_field(name='The following error occured while running this command',
							value='MissingRequiredArgument', inline=False)
			embed.add_field(name='Please redo the command with all the parameters',
							value='`eg.` `+embed [title] [text]`', inline=False)
			embed.set_footer(text=f'| {ctx.message.author.name} | If you belive this is a error, please DM HelloWorld#7091')
			await ctx.channel.send(embed=embed, delete_after=10)

		else:
			await ctx.send(f"Oops! An error occured while running your command. {error}")
			raise(error)


def setup(client):
	client.add_cog(Events(client))
