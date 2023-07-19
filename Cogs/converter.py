import discord
from discord.ext import commands


class Converter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send("Helloww")


async def setup(bot):
    await bot.add_cog(Converter(bot))
