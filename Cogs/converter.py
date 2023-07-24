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

    @commands.command(aliases=['g'], description="Unguessable")
    async def guess(self, ctx, x: int):
        temp = random.randint(1, 10)
        if x == temp:
            await ctx.send(f"your gues is Correct {ctx.author.display_name} haha")

        elif x > temp:
            await ctx.send(f"your gues is too big  {ctx.author.display_name} haha")

        elif x < temp:
            await ctx.send(f"your gues is too low  {ctx.author.display_name} haha")
        else:
            await ctx.send(f"Your guess is wrong  dude{ctx.author.display_name}")

    @commands.command()
    async def subtract(self, ctx, number: int):
        randoms = random.randint(0, 100)
        await ctx.send(number - randoms)

    @commands.command(aliases=["join"])
    async def joined(self, ctx, member: discord.Member):
        if member in member.guild.members:
            await ctx.send(
                f"Member of {member.guild.name} with name {member.display_name} joined at {member.joined_at}")

    # error
    @commands.command(aliases=['count'])
    async def member_count(self, ctx, member: discord.Member):
        total = 0
        members = discord.Member
        for member in members.guild:
            member = total + 1
            await ctx.send(f"There are {member} members")


async def setup(bot):
    await bot.add_cog(Converter(bot))
    print("Loaded Converter extension")
