import discord
from discord.ext import commands
import random


class Converter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def peng(self, ctx):
        await ctx.send(f"Helloww {ctx.author.display_name} from cogs")

    @commands.command()
    async def avatar(self, ctx, member: discord.Member):
        await ctx.send(f"{member.display_avatar}")

    @commands.command()
    async def search(self, ctx, member: discord.Member):
        if member in member.guild.members:
            await ctx.send(f"Huhhhhh {member.display_name} found!!!")
        else:
            await ctx.send(f"Hmm{member.display_name} not found :(")

    @commands.command(aliases=['fav'])
    async def favArtist(self, ctx):
        botFav = ["Yoasobi", "Imase", "Deny Caknan", "JVKE"]
        choice = random.choice(botFav)
        await ctx.send(f"Hmm my favorite is...................{choice}")

    @commands.command(aliases=['g'])
    async def guess(self, ctx, x: int):
        temp = random.randint(1, 100)
        if x != temp:
            await ctx.send(f"your gues is Wrong {ctx.author.display_name} haha, the correct answer is {temp} ")

        else:
            await ctx.send(f"Your guess is true dude{ctx.author.display_name}")

    @commands.command()
    async def subtract(self, number: int, ctx):
        randoms = random.randint(0, 1000)
        await ctx.send(number - randoms)

    @commands.command(aliases=["join"])
    async def joined(self, ctx, member: discord.Member):
        if member in member.guild.members:
            await ctx.send(
                f"Member of {member.guild.name} with name {member.display_name} joined at {member.joined_at}")


async def setup(bot):
    await bot.add_cog(Converter(bot))
