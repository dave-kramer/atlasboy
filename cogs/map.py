import discord
import datetime

from discord.ext import commands


class Map(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    description = 'Return a certain island.'
    
    @commands.command(name='map')
    async def map(self, ctx):
        embed = discord.Embed(title=f'Map', url='https://atlas.antihax.net/', color=0x87CEEB)
        file = discord.File(f"grid-img/WorldMap.png", filename=f"WorldMap.png")
        embed.set_image(url=f"attachment://WorldMap.png")
        embed.set_footer(text="Requested by: {}".format(ctx.author.display_name), icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed, file=file)
        

# adding cog to bot setup
def setup(bot):
	bot.add_cog(Map(bot))