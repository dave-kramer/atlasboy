import discord
import datetime

import json

from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument


class Animal(commands.Cog):
        
    def __init__(self, client):
        self.client = client
    description = 'Get information about a certain animal.'
        
    @commands.command(name='animal')
    async def animal(self, ctx, arg: str):
        with open('json/animals.json') as f:
            data = json.load(f)
            arg = arg.title()
            data = data['Animals']
            if f'{arg}' not in data:
                await ctx.send('That is not an animal in Atlas.')
            else:
                embed = discord.Embed(title=f"{arg}", color=0x87CEEB)
                if 'XP' not in data[f'{arg}']:
                    embed.add_field(name=f"XP", value=f"{arg}", inline=True)
                elif not data[f'{arg}']['XP']:
                    embed.add_field(name=f"XP", value=f"{arg}", inline=True)
                else:
                    embed.add_field(name=f"XP", value=f"{round(data[f'{arg}']['XP'], 3)}", inline=True)
                embed.add_field(name=f"XP per hit", value=f"{data[f'{arg}']['XPperHit']}", inline=True)
                if data[f'{arg}']['canBeTamed'] == True:
                    embed.add_field(name=f"Tame", value=f"Yes", inline=True)
                else:
                    embed.add_field(name=f"Tame", value=f"No", inline=True)
                embed.add_field(name=f"Preference", value=f"{data[f'{arg}']['foodPreference']}", inline=True)
                embed.add_field(name=f"Min breed temp", value=f"{data[f'{arg}']['minTemperatureToBreed']}", inline=True)
                embed.add_field(name=f"Max breed temp", value=f"{data[f'{arg}']['maxTemperatureToBreed']}", inline=True)
                embed.add_field(name=f"Breed interval", value=f"{data[f'{arg}']['tameConsumeInterval']}", inline=True)
                #embed.add_field(name=f"Food", value=f"{data[f'{arg}']['food']}", inline=True)
                if 'resources' not in data[f'{arg}']:
                    embed.add_field(name=f"Drops", value=f"None", inline=True)
                elif not data[f'{arg}']['resources']:
                    embed.add_field(name=f"Drops", value=f"None", inline=True)
                else:
                    resource_string = ", ".join(data[f'{arg}']['resources'])
                    embed.add_field(name=f"Drops", value=f"{resource_string}", inline=False)
                embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)


# adding cog to bot setup
def setup(bot):
    bot.add_cog(Animal(bot))