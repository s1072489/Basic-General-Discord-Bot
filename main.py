import os
import discord_components
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType, component

TOKEN = os.environ['TOKEN']
client = commands.Bot(command_prefix="+", case_insensitive=True)
# client.remove_command('help')
DiscordComponents(client)


for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")
print("All Cogs loaded successfully")

@client.command()
async def restart(ctx):
	await ctx.message.delete()
	if ctx.message.author.id == 825232373481865226:
		for filename in os.listdir("./cogs"):
			if filename.endswith(".py"):
				client.reload_extension(f"cogs.{filename[:-3]}")
		print("Bot restarted successfully")
		await ctx.send("Bot restarted successfully")
	else:
		await ctx.send("Not owner of bot!")

client.run(TOKEN)
