import discord
import datetime

import json

from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument


class Item(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    description = 'Returns information about a certain item.'
    
    @commands.command(name='item')
    async def item(self, ctx, *, arg: str):
        with open('json/items.json') as f:
            data = json.load(f)
            arg = arg.title()
            if f'{arg}' not in data:
                await ctx.send('That is not an item in Atlas.')
            else:
                embed = discord.Embed(title=f"{arg}", color=0x87CEEB)
                #embed.add_field(name=f"{arg}", value=f"{data[f'{arg}']}", inline=False)
                if 'Type' not in data[f'{arg}']:
                    embed.add_field(name=f"Type", value="None", inline=True)
                elif not data[f'{arg}']['Type']:
                    embed.add_field(name=f"Type", value="None", inline=True)
                else:
                    embed.add_field(name=f"Type", value=f"{data[f'{arg}']['Type']}", inline=True)
                if 'Ingredients' not in data[f'{arg}']:
                    embed.add_field(name=f"Ingredients", value="None", inline=True)
                elif not data[f'{arg}']['Ingredients']:
                    embed.add_field(name=f"Ingredients", value="None", inline=True)
                else:
                    string = ", ".join(data[f'{arg}']['Ingredients'])
                    embed.add_field(name=f"Ingredients", value=f"{string}", inline=True)
                if 'SpoilTime' not in data[f'{arg}']:
                    embed.add_field(name=f"Spoil time", value="None", inline=True)
                elif not data[f'{arg}']['SpoilTime']:
                    embed.add_field(name=f"Spoil time", value="None", inline=True)
                else:
                    embed.add_field(name=f"Spoil time", value=f"{data[f'{arg}']['SpoilTime']}", inline=True)
                if 'Weight' not in data[f'{arg}']:
                    embed.add_field(name=f"Weight", value="None", inline=True)
                elif not data[f'{arg}']['Weight']:
                    embed.add_field(name=f"Weight", value="None", inline=True)
                else:
                    embed.add_field(name=f"Weight", value=f"{data[f'{arg}']['Weight']}", inline=True)
                if 'Icon' not in data[f'{arg}']:
                    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png")
                    embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                    embed.timestamp = datetime.datetime.utcnow()
                    await ctx.send(embed=embed)
                else:
                    file = discord.File(f"atlas-icons/{data[f'{arg}']['Icon']}_128.png", filename=f"{data[f'{arg}']['Icon']}_128.png")
                    embed.set_image(url=f"attachment://{data[f'{arg}']['Icon']}_128.png")
                    embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                    embed.timestamp = datetime.datetime.utcnow()
                    await ctx.send(embed=embed, file=file)


# adding cog to bot setup
def setup(bot):
	bot.add_cog(Item(bot))