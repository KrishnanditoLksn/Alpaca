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
    async def favoriteArtist(self, ctx):
        botFav = ["Yoasobi", "Imase", "Deny Caknan", "JVKE"]
        choice = random.choice(botFav)
        await ctx.send(f"Hmm my favorite is...................{choice}")

    @commands.command(aliases=['guess'], description="Unguessable")
    async def randomGuessNumber(self, ctx, x: int):
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
    @commands.cooldown(1, 5)
    async def joined(self, ctx, member: discord.Member):
        if member in member.guild.members:
            await ctx.send(
                f"Member of {member.guild.name} with name {member.display_name} joined at {member.joined_at}")

    @commands.command()
    async def repeated(self, ctx, times: int):
        """im looping!!"""
        for i in range(times):
            await ctx.send(f"I'm looping {ctx.author.mention}")

    @commands.command()
    async def pam(self, ctx, member: discord.Member):

        for looper in range(3):
            if member in member.guild.members:
                await ctx.send(f"{member.display_avatar}")

    @commands.command()
    @commands.cooldown(2, 5)
    async def troll(self, ctx, choice: int):
        link = "https://youtu.be/ZRtdQ81jPUQ"
        if choice == 1:
            await ctx.send(f"The best of the best{link}")

        elif choice == 2:
            gif = ["https://cdn.discordapp.com/attachments/981882727852802058/1135209597636984832/8847-cr7-siuu.gif",
                   "https://cdn.discordapp.com/attachments/1114027418118795387/1135954604538994838/rickroll.gif",
                   "https://cdn.discordapp.com/attachments/1119903704561238157/1135957132240507031/oshi-no-ko-skill"
                   "-issue.gif"]
            randomDescription = ["Siuuu", "Never gonna give you...", "Cielah bucinnn", "huu Wibu", "Rapsodiiii"]

            for looper in range(5):
                embeds = discord.Embed(colour=(discord.Colour.random()),
                                       description=f"{random.choice(randomDescription)},"f"{ctx.author.mention}")
                embeds.set_image(url=random.choice(gif))
                await ctx.send(embed=embeds)

        else:
            await ctx.send("Invalid cok")

    """"@commands.command(aliases=['ngp'])
    async def ngapain(self, ctx, member: discord.Member):

        if member in member.guild:
            await ctx.send(f"Hmmmmm {member.display_name} ternyata  {member.premium_since}")

        else:
            await ctx.send(f"Yahh {member.name} ga ada")"""""

    @commands.command(aliases=['count'])
    async def memberCount(self, ctx):
        await ctx.send(ctx.guild.member_count)


async def setup(bot):
    await bot.add_cog(Converter(bot))
    print("Loaded Converter extension")
