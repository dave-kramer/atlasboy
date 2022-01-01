import discord
import datetime

from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument
from all import gridinfo_list, grid_list


class Grid(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    description = 'Returns all islands on a grid.'
    
    @commands.command(name='grid')
    async def grid(self, ctx, *, arg: str):
            
            arg = arg.title()
           
            if f'{arg}' not in grid_list:
                await ctx.send('That is not a grid in Atlas.')
            
            else:
                
                embed = discord.Embed(title=f"{arg}",description="ControlPoints are only shown on map. ", color=0x87CEEB)
                file = discord.File(f"grid-img/{arg}.png", filename=f"{arg}.png")
                embed.set_image(url=f"attachment://{arg}.png")
                
                await ctx.send(embed=embed, file=file)
                
                for length in gridinfo_list:
                    for key in length:
                        if key == f'{arg}':
                           
                            embed = discord.Embed(title=f"{length[key][0]}", color=0x87CEEB)
                            embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                            embed.timestamp = datetime.datetime.utcnow()
                            file = discord.File(f"island-img/{length[key][1]}.webp", filename=f"{length[key][1]}.webp")
                            embed.set_thumbnail(url=f"attachment://{length[key][1]}.webp")
                            
                            await ctx.send(embed=embed, file=file)

                        else:
                            continue

                    else:
                        continue


# adding cog to bot setup
def setup(bot):
    bot.add_cog(Grid(bot))