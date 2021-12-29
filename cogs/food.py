import discord
import datetime

import json

from discord.ext import commands


class Food(commands.Cog):
        
    def __init__(self, client):
        self.client = client
    description = 'Get information about a certain animal.'
        
    @commands.command(name='food')
    async def food(self, ctx, *, arg: str):
        with open('json/craftables.json') as f:
            data = json.load(f)
            arg = arg.title()
            for length in data['Foods']:
                if f'{arg}' == length:
                    embed = discord.Embed(title=f"{arg}", color=0x87CEEB)
                    if not data['Foods'][length]['Type']:
                        embed.add_field(name=f"Type", value=f"None", inline=True)
                    else:
                        embed.add_field(name=f"Type", value=f"{data['Foods'][length]['Type']}", inline=True)
                    embed.add_field(name=f"Weight", value=f"{round(data['Foods'][length]['Weight'], 3)}", inline=True)
                    embed.add_field(name=f"Spoil time", value=f"{data['Foods'][length]['SpoilTime']}", inline=True)
                    embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                    embed.timestamp = datetime.datetime.utcnow()
                    await ctx.send(embed=embed)


# adding cog to bot setup
def setup(bot):
    bot.add_cog(Food(bot))