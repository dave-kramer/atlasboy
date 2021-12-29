import discord
import datetime

import json

from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument


with open('json/islands.json') as f:
	data = json.load(f)
grid_check = []
for length in data:
	grid = data[length]['grid']
	if grid in grid_check:
		continue
	else:
		grid_check.append(grid)


class Grid(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    description = 'Returns all islands on a grid.'
    
    @commands.command(name='grid')
    async def grid(self, ctx, *, arg: str):
        with open('json/islands.json') as f:
            data = json.load(f)
            arg = arg.title()
            if f'{arg}' not in grid_check:
                await ctx.send('That is not a grid in Atlas.')
            else:
                embed = discord.Embed(title=f"{arg}",description="ControlPoints are only shown on map.", color=0x87CEEB)
                file = discord.File(f"grid-img/{arg}.png", filename=f"{arg}.png")
                embed.set_image(url=f"attachment://{arg}.png")
                await ctx.send(embed=embed, file=file)
                for length in data:
                    grid = data[length]['grid']
                    if arg == grid:
                        if 'discoveries' not in data[length]:
                            embed = discord.Embed(title=f"{data[length]['name']}", color=0x87CEEB)
                        elif not data[length]['discoveries']:
                            embed = discord.Embed(title=f"{data[length]['name']}", color=0x87CEEB)
                        else:
                            embed = discord.Embed(title=f"{data[length]['discoveries'][0]['name']}", color=0x87CEEB)
                        if data[length]['name'] == 'ControlPoint':
                            continue
                            #embed = discord.Embed(title=f"{data[length]['name']}",description="This is a Control Point", color=0x87CEEB)
                            #embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                            #embed.timestamp = datetime.datetime.utcnow()
                            #await ctx.send(embed=embed)
                        else:
                            #embed.add_field(name=f"Resources", value=f"{data[length]['resources']}", inline=False)
                            #embed.add_field(name=f"Animals", value=f"{data[length]['animals']}", inline=False)
                            embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                            embed.timestamp = datetime.datetime.utcnow()
                            file = discord.File(f"island-img/{data[length]['name']}.webp", filename=f"{data[length]['name']}.webp")
                            embed.set_thumbnail(url=f"attachment://{data[length]['name']}.webp")
                            await ctx.send(embed=embed, file=file)
                    else:
                        continue


# adding cog to bot setup
def setup(bot):
    bot.add_cog(Grid(bot))