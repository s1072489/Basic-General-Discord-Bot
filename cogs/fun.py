import discord
import random
import asyncio
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType, component
from discord.ext import commands


class Fun(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command(aliases=["hello", "greet"])
	async def hi(self, ctx):
		await ctx.message.delete()
		await ctx.send("Say hello!", delete_after=15)

		def check(m):
			val = False
			if "hello" in str(m.content).lower() and m.channel == ctx.channel:
				val = True
			elif "hi" in str(m.content).lower() and m.channel == ctx.channel:
				val = True
			return(val)

		msg = await self.client.wait_for("message", check=check, timeout=15)
		await ctx.send(f"Hello {msg.author}!")


	@commands.command(aliases=['roll'])
	async def dice(self, ctx):
		await ctx.message.delete()
		await ctx.send(f'And the dice lands on.... {random.randint(1,6)}!')


	@commands.command(pass_content=True)
	async def id(self, ctx, user: discord.Member):
		await ctx.send(f"{user}'s id is {user.id}")
		await ctx.message.delete()


	@commands.command(aliases=["msg", "message"])
	@commands.cooldown(1, 5, commands.BucketType.user)
	async def send(self, ctx, user: discord.Member, *, msg):
		if user == ctx.message.author:
			await ctx.send("You... want to send a message to yourself?")
		else:
			try:
				emb = discord.Embed(
					colour=discord.Colour.blue()
				)
				emb.add_field(name=f"Message recived from {ctx.message.guild.name}", value=f"{msg}")
				emb.set_footer(text=f"Message sent by {ctx.message.author}")
				await user.send(embed=emb)

				embed = discord.Embed(
					colour=discord.Colour.green()
				)
				embed.add_field(name=f"Message sent to {user} from {ctx.message.author}", value=f"{msg}")
				await ctx.channel.send(embed=embed)
				await ctx.message.delete()
			except:
				emer = discord.Embed(
					color=discord.Colour.red()
				)
				emer.set_author(name="Aww Snap! Something went wrong..")
				emer.set_footer(
					text="This may be because the recepient has closed DMs or the message was too long")
				await ctx.send(embed=emer)

	@commands.command()
	async def game(self, ctx):
		await ctx.message.delete()
		game = ['rock', 'paper', 'scissors', 'quit']
		score = [0, 0]
		outcomes = {
			"rock": {"win": "paper", "draw": "rock", "lose": "scissors"},
			"paper": {"win": "scissors", "draw": "paper", "lose": "rock"},
			"scissors": {"win": "rock", "draw": "scissors", "lose": "paper"}
		}

		while True:
			botmsg = await ctx.channel.send(f"Rock paper scissors? {ctx.message.author}", components=[[Button(style=ButtonStyle.blue, label="Rock"), Button(style=ButtonStyle.green, label="Paper"), Button(style=ButtonStyle.grey, label="Scissors"), Button(style=ButtonStyle.red, label="Quit")]], delete_after=15)

			def check(m):
				return m.author == ctx.author

			try:
				res = await self.client.wait_for("button_click", check=check, timeout=15)
			except asyncio.TimeoutError:
				await ctx.send("Timeout!", delete_after=5)
				res.component.label = "quit"
						
			user = res.component.label.lower()
			try:
				await botmsg.delete()
			except:
				pass

			if user == "quit":
				if
				embed = discord.Embed()
				embed.set_author(name=f"Game ended with {ctx.message.author.name}.")
				embed.add_field(name="Your score:", value=f"`{score[1]}`", inline=True)
				embed.add_field(name="My score:", value=f"`{score[0]}`", inline=True)
				await ctx.send(embed=embed)
				break
			else:
				outcome = random.choice(["win", "draw", "lose"])
				comp = outcomes[user][outcome]

				if outcome == "win":
					colour = discord.Colour.red()
					score[0] += 1
					text = "You lose!"
				elif outcome == "draw":
					colour = discord.Colour.orange()
					text = "Draw!"
				else:
					colour = discord.Colour.green()
					score[1] += 1
					text = "You win!"

				embed = discord.Embed(colour=colour)
				embed.set_author(name=text)
				embed.add_field(name="Your choice:", value=f"`{user.capitalize()}`", inline=True)
				embed.add_field(name="My choice:", value=f"`{comp.capitalize()}`", inline=True)
				embed.set_footer(text=f"{ctx.message.author.name}: {score[1]} - Gigabyte: {score[0]}")
				await ctx.send(embed=embed)

def setup(client):
	client.add_cog(Fun(client))
