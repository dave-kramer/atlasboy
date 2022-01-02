import discord
import datetime

from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument
from all import islandinfo_list


class Island(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    description = 'Return a certain island.'
    
    @commands.command(name='island')
    async def island(self, ctx, *, arg: str):
            arg = arg.title()

            for length in islandinfo_list:
                for key in length:
                    if key == f'{arg}':
                        
                            embed = discord.Embed(title=f"{arg}", color=0x87CEEB)
                            embed.add_field(name=f"ID", value=f"{length[key][0]}", inline=True)
                            
                            if not length[key][1]:
                                embed.add_field(name=f"Region", value="None", inline=True)
                            else:
                                embed.add_field(name=f"Region", value=f"{length[key][1]}", inline=True)

                            embed.add_field(name=f"Grid", value=f"{length[key][2]}", inline=True)
                            embed.add_field(name=f"Biomes", value=f"{length[key][3]}", inline=False)
                            embed.add_field(name=f"Animals", value=f"{length[key][4]}", inline=False)
                            embed.add_field(name=f"Resources", value=f"{length[key][5]}", inline=False)

                            file = discord.File(f"island-img/{length[key][0]}.webp", filename=f"{length[key][0]}.webp")
                            embed.set_thumbnail(url=f"attachment://{length[key][0]}.webp")
                            embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                            embed.timestamp = datetime.datetime.utcnow()

                            await ctx.send(embed=embed, file=file)


# adding cog to bot setup
def setup(bot):
    bot.add_cog(Island(bot))