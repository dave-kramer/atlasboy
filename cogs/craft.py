import discord
import datetime

import json

from discord.ext import commands


class Craft(commands.Cog):
        
    def __init__(self, client):
        self.client = client
    description = 'Get information about a certain animal.'
        
    @commands.command(name='craft')
    async def craft(self, ctx, *, arg: str):
        with open('json/craftables.json') as f:
            data = json.load(f)
            arg = arg.title()
            for length in data['Craftables']:
                if f'{arg}' == length:
                    embed = discord.Embed(title=f"{arg}", color=0x87CEEB)
                    for i in data['Craftables'][length]['Ingredients']:
                        embed.add_field(name=f"{i}", value=f"{round(data['Craftables'][length]['Ingredients'][i])}", inline=True)
                    embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                    embed.timestamp = datetime.datetime.utcnow()
                    await ctx.send(embed=embed)


# adding cog to bot setup
def setup(bot):
    bot.add_cog(Craft(bot))