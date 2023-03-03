import discord
import os
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
intents = discord.Intents().all()

intents.message_content = True
bot = discord.Bot()


@bot.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(bot))

@bot.command(name="firstslash", description="Sends the bot's latency.")
async def first_slash(ctx): 
    await ctx.respond("You executed the slash command!")


@bot.command(description="Sends the bot's latency.")
async def first_slash(ctx): 
    await ctx.respond("You executed the slash command!")



bot.run(token)