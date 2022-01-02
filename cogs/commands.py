import discord

from discord.ext import commands


class Commands(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='commands')
    async def commands(self, ctx):
        
        embed = discord.Embed(title=f"Commands", color=0x87CEEB)

        embed.add_field(name=";animal name", value="Gives you the XP, XP per hit, tame, preference, min & max breed temp, breed interval and drops.\nExample: ;animal chicken", inline=False)
        embed.add_field(name=";grid name", value="Gives you the map and the islands on the grid.\nExample: ;grid a4", inline=False)
        embed.add_field(name=";island name", value="Gives you the ID, region, grid, biomes, animals and resources.\nExample: ;island The Haunted Key", inline=False)
        embed.add_field(name=";item name", value="Gives you the type, ingredients, spoil time and weight.\nExample: ;item fish meat", inline=False)
        embed.add_field(name=";craft name", value="Gives you amount required to craft.\nExample: ;craft schooner", inline=False)
        embed.add_field(name=";food name", value="Gives you information about the food.\nExample: ;food stimberry", inline=False)
        embed.add_field(name=";map", value="Gives you the full map of Atlas.", inline=False)

        await ctx.author.send(embed=embed)


# adding cog to bot setup
def setup(bot):
    bot.add_cog(Commands(bot))