import random

import discord
from discord.ext import commands
from discord import app_commands


class randomEmbeds(commands.Cog):

    # fill  information about Alpacaa bot

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['ask1'])
    async def askBot(self, ctx):
        embed1 = discord.Embed(
            title="Information",
            colour=(discord.Colour.random()),
            description=f"Hey hey this is bot"
        )
        embed1.set_thumbnail(url="https://cdn.discordapp.com/attachments/1131584535063187586/1135220891748401183/alpa"
                                 ".png")
        await ctx.send(embed=embed1)


async def setup(bot: commands.Bot):
    await bot.add_cog(randomEmbeds(bot))
    print("Loaded Embeds extension")
