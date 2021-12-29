import discord
import datetime

import json

from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument


class Island(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    description = 'Return a certain island.'
    
    @commands.command(name='island')
    async def island(self, ctx, *, arg: str):
        with open('json/islands.json') as f:
            data = json.load(f)
            arg = arg.title()

            for length in data:
                if not data[length]['discoveries']:
                    continue
                else:
                    if arg == data[length]['discoveries'][0]['name']:
                        embed = discord.Embed(title=f"{data[length]['discoveries'][0]['name']}", color=0x87CEEB)
                        embed.add_field(name=f"ID", value=f"{data[length]['name']}", inline=True)
                        if not data[length]['region']:
                            embed.add_field(name=f"Region", value="None", inline=True)
                        else:
                            embed.add_field(name=f"Region", value=f"{data[length]['region']}", inline=True)
                        embed.add_field(name=f"Grid", value=f"{data[length]['grid']}", inline=True)
                        biomes_string = ', '.join(data[length]['biomeTags'])
                        embed.add_field(name=f"Biomes", value=f"{biomes_string}", inline=False)
                        animal_string = ', '.join(data[length]['animals'])
                        embed.add_field(name=f"Animals", value=f"{animal_string}", inline=False)
                        resource_string = ', '.join(data[length]['resources'])
                        embed.add_field(name=f"Resources", value=f"{resource_string}", inline=False)
                        file = discord.File(f"island-img/{data[length]['name']}.webp", filename=f"{data[length]['name']}.webp")
                        embed.set_thumbnail(url=f"attachment://{data[length]['name']}.webp")
                        embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                        embed.timestamp = datetime.datetime.utcnow()
                        await ctx.send(embed=embed, file=file)

                    

# adding cog to bot setup
def setup(bot):
    bot.add_cog(Island(bot))