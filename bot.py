from datetime import datetime, timezone

import discord
import os
import random

from discord import app_commands
from discord.app_commands import checks
from dotenv import load_dotenv
from discord.ext import commands
from interactions.api.http import interaction

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
intents = discord.Intents().all()

intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents, default=False)

@bot.hybrid_command(name='hello', description='Gives time')
async def hello(ctx):
    await ctx.send(f"It is {datetime.now(timezone.utc)} UTC.")


@bot.hybrid_command(name='meow')
async def meow(ctx):
    await ctx.send("You executed the slash command!")

@bot.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(bot))
    await bot.tree.sync()
    await bot.change_presence(activity=discord.activity.Game(name='blah'), status=discord.Status.do_not_disturb)
    print("Online!")
    bot.tree.command(name="hello", description="lorem ipsum")

bot.run(token)