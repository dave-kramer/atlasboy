import discord
import datetime

from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument
from all import animal_list


class Animal(commands.Cog):
        
    def __init__(self, client):
        self.client = client
    description = 'Get information about a certain animal.'
        
    @commands.command(name='animal')
    async def animal(self, ctx, arg: str):
        arg = arg.title()

        for length in animal_list:
            if f'{arg}' == length:

                embed = discord.Embed(title=f"{arg}", color=0x87CEEB)
                if 'XP' not in animal_list[length] or not animal_list[length]['XP']:
                    embed.add_field(name=f"XP", value=f"{arg}", inline=True)
                else:
                    embed.add_field(name=f"XP", value=f"{round(animal_list[length]['XP'], 3)}", inline=True)

                embed.add_field(name=f"XP per hit", value=f"{animal_list[length]['XPperHit']}", inline=True)
                if animal_list[length]['canBeTamed'] == True:
                    embed.add_field(name=f"Tame", value=f"Yes", inline=True)
                else:
                    embed.add_field(name=f"Tame", value=f"No", inline=True)

                embed.add_field(name=f"Preference", value=f"{animal_list[length]['foodPreference']}", inline=True)
                embed.add_field(name=f"Min breed temp", value=f"{animal_list[length]['minTemperatureToBreed']}", inline=True)
                embed.add_field(name=f"Max breed temp", value=f"{animal_list[length]['maxTemperatureToBreed']}", inline=True)
                embed.add_field(name=f"Breed interval", value=f"{animal_list[length]['tameConsumeInterval']}", inline=True)
                #embed.add_field(name=f"Food", value=f"{animal_list[length]['food']}", inline=True)

                if 'resources' not in animal_list[length] or not animal_list[length]['resources']:
                    embed.add_field(name=f"Drops", value=f"None", inline=True)
                else:
                    resource_string = ", ".join(animal_list[length]['resources'])
                    embed.add_field(name=f"Drops", value=f"{resource_string}", inline=False)

                embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                embed.timestamp = datetime.datetime.utcnow()

                await ctx.send(embed=embed)


# adding cog to bot setup
def setup(bot):
    bot.add_cog(Animal(bot))