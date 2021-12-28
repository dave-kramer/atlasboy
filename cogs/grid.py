import discord
import datetime

import json

from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument


class Grid(commands.Cog):
    
	def __init__(self, client):
		self.client = client
	description = 'Get information about a certain grid.'
    
	@commands.command(name='grid')
	async def grid(self, ctx, arg: str):
		with open('json/gridList.json') as f:
			data = json.load(f)
			arg = arg.title()
			if f'{arg}' not in data:
				await ctx.send('That is not a grid in Atlas.')
			else:
				animal_string = ", ".join(data[f'{arg}']['animals'])
				biomes_string = ", ".join(data[f'{arg}']['biomes'])
				resources_string = ", ".join(data[f'{arg}']['resources'])
				embed = discord.Embed(title=f"Grid {arg}", color=0x87CEEB)
				if 'Name' not in data[f'{arg}']:
					embed.add_field(name=f"Name", value=f"{arg}", inline=True)
				elif not data[f'{arg}']['Name']:
					embed.add_field(name=f"Name", value=f"{arg}", inline=True)
				else:
					embed.add_field(name=f"Name", value=f"{arg}", inline=True)
				if not data[f'{arg}']['region']:
					embed.add_field(name=f"Region", value="None", inline=True)
				else:
					embed.add_field(name=f"Region", value=f"{data[f'{arg}']['region']}", inline=True)
				embed.add_field(name=f"Animals", value=f"{animal_string}", inline=False)
				embed.add_field(name=f"Biomes", value=f"{biomes_string}", inline=False)
				embed.add_field(name=f"Resources", value=f"{resources_string}", inline=False)
				embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
				embed.timestamp = datetime.datetime.utcnow()
				await ctx.send(embed=embed)


# adding cog to bot setup
def setup(bot):
	bot.add_cog(Grid(bot))