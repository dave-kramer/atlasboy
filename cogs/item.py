import discord
import datetime

from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument
from all import item_list


class Item(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    description = 'Returns information about a certain item.'
    
    @commands.command(name='item')
    async def item(self, ctx, *, arg: str):

            arg = arg.title()

            for length in item_list:
                if f'{arg}' == length:

                    embed = discord.Embed(title=f"{arg}", color=0x87CEEB)

                    if 'Type' not in item_list[length] or not item_list[length]['Type']:
                        embed.add_field(name=f"Type", value="None", inline=True)
                    else:
                        embed.add_field(name=f"Type", value=f"{item_list[length]['Type']}", inline=True)

                    if 'SpoilTime' not in item_list[length] or not item_list[length]['SpoilTime']:
                        embed.add_field(name=f"Spoil time", value="None", inline=True)
                    else:
                        embed.add_field(name=f"Spoil time", value=f"{round(item_list[length]['SpoilTime'])}", inline=True)

                    if 'Weight' not in item_list[length] or not item_list[length]['Weight']:
                        embed.add_field(name=f"Weight", value="None", inline=True)
                    else:
                        embed.add_field(name=f"Weight", value=f"{round(item_list[length]['Weight'], 2)}", inline=True)

                    if 'Ingredients' not in item_list[length] or not item_list[length]['Ingredients']:
                        embed.add_field(name=f"Ingredients", value="None", inline=True)
                    else:
                        for i in item_list[length]['Ingredients']:
                            embed.add_field(name=f"{i}", value=f"{round(item_list[length]['Ingredients'][i])}", inline=True)

                    if 'Icon' not in item_list[length]:
                        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png")
                        embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                        embed.timestamp = datetime.datetime.utcnow()
                        
                        await ctx.send(embed=embed)

                    else:
                        file = discord.File(f"atlas-icons/{item_list[length]['Icon']}_128.png", filename=f"{item_list[length]['Icon']}_128.png")
                        embed.set_image(url=f"attachment://{item_list[length]['Icon']}_128.png")
                        embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                        embed.timestamp = datetime.datetime.utcnow()

                        await ctx.send(embed=embed, file=file)


# adding cog to bot setup
def setup(bot):
	bot.add_cog(Item(bot))