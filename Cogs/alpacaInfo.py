import random
from discord.ext import commands


class AlpacaInfo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['fact'])
    async def alpacaFact(self, ctx):
        factList = ["#1 They are in fact NOT small llamas,"
                    "#2 They are short and bulky.",
                    "#3 They come in two breeds: suri and haucaya,"
                    "#4 They communicate through body language,",
                    "#5 They also use sounds to communicate,",
                    "#6 They sometimes use spitting as a defense,",
                    "#7 They are clean freaks."]
        randomFact = random.choice(factList)
        await ctx.send(randomFact)


async def setup(bot: commands.Bot):
    await bot.add_cog(AlpacaInfo(bot))
    print("Loaded core information extension")
