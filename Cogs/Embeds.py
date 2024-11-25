import discord
from discord.ext import commands


class RandomEmbeds(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['ask1'])
    async def askBot(self, ctx):
        embed1 = discord.Embed(
            title="Alpaca",
            colour=(discord.Colour.random()),
            description="Hey hey this is bot"
        )
        embed1.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/1131584535063187586/1135220891748401183/alpa.png")
        await ctx.send(embed=embed1)

    @commands.command(aliases=['ask2'])
    async def askAuthor(self, ctx):
        await ctx.send()

    @commands.command(aliases=['ask3'])
    async def displayYourEmbed(self, ctx, member: discord.Member):
        embeds = discord.Embed(
            title=f"Semangatttt : {member.display_name}",
            description=f" Anjay lagi  : {member.activity.name}"
        )
        await ctx.send(embed=embeds)


async def setup(bot: commands.Bot):
    await bot.add_cog(RandomEmbeds(bot))
    print("Loaded Embeds extension")
