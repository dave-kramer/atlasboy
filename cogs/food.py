import discord
import datetime

from discord.ext import commands
from all import food_list


class Food(commands.Cog):
        
    def __init__(self, client):
        self.client = client
    description = 'Get information about a certain animal.'
        
    @commands.command(name='food')
    async def food(self, ctx, *, arg: str):
        arg = arg.title()

        for length in food_list[0]:
            if f'{arg}' == length:

                embed = discord.Embed(title=f"{arg}", color=0x87CEEB)

                if not food_list[0][length]['Type']:
                    embed.add_field(name=f"Type", value=f"None", inline=True)
                else:
                    embed.add_field(name=f"Type", value=f"{food_list[0][length]['Type']}", inline=True)

                embed.add_field(name=f"Weight", value=f"{round(food_list[0][length]['Weight'], 3)}", inline=True)
                embed.add_field(name=f"Spoil time", value=f"{food_list[0][length]['SpoilTime']}", inline=True)
                
                embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                embed.timestamp = datetime.datetime.utcnow()

                await ctx.send(embed=embed)


# adding cog to bot setup
def setup(bot):
    bot.add_cog(Food(bot))