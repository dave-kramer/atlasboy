import discord
import os
import random
import asyncio

from dotenv import load_dotenv
from discord.ext import commands

"""
Make sure to put YOUR bot token inside a new .env file otherwise the bot won't load.
"""
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client = commands.Bot(command_prefix = ';')


for filename in os.listdir('./cogs'):
    """
    | Loading all the available cogs
    """
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Unknown command use ;commands.")


@client.event
async def on_ready():
    """
    | Activity of the discord bot
    """
    await client.change_presence(activity=discord.Game(name="on the sea"))
    print('AtlasBoy is online.')


async def ch_pr():
    await client.wait_until_ready()
    """
    | Add multiple statuses by changing inbetween the "" or adding the , and putting more "" before the ]
    """
    statuses = ["with bear poo", ";commands", "with the parrot"]

    while not client.is_closed():
        status = random.choice(statuses)
        await client.change_presence(activity=discord.Game(name=status))
        """
        | You can change the timer for activity by replacing the 120 (2minutes) with for example 60 (1minute) just make sure to put it in seconds.
        """
        await asyncio.sleep(120)

client.loop.create_task(ch_pr())

"""
Bot run.
"""
client.run(TOKEN)
