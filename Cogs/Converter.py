import aiohttp
import discord
from discord.ext import commands
import random
from requests import get
import json


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
        bot_fav = ["Yoasobi", "Imase", "Deny Caknan", "JVKE"]
        choice = random.choice(bot_fav)
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
            random_description = ["Siuuu", "Never gonna give you...", "Cielah bucinnn", "huu Wibu", "Rapsodiiii"]

            for i in range(5):
                embeds = discord.Embed(colour=(discord.Colour.random()),
                                       description=f"{random.choice(random_description)} {ctx.author.mention}")
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

    @commands.command(aliases=['gf'])
    async def randomGirlFriendAsking(self, ctx, choice: str):
        girl_friend_list = ['Tatsumaki', 'Kaori', 'Rick Astley', 'Saitama', 'Shizuka']
        love_emoji = '👿'

        if choice.__eq__('yes'):
            await ctx.send(random.choice(girl_friend_list))

        else:
            message = await ctx.send(f" boyfriend with {girl_friend_list[2]}")
            await message.add_reaction(love_emoji)

    @commands.command(aliases=['suhu'])
    async def digitalThermometerConverter(self, ctx, suhu: int):
        celsius_fahrenheit = (suhu * 9 / 5) + 32
        """buat converter suhu dengan meminta input user bertipe int """
        wrong_emoji = '❌'

        if suhu < 0:
            message = await ctx.send("Hmm think again!!")
            await message.add_reaction(wrong_emoji)

        else:
            await ctx.send(f"Celsius -> Fahrenheit : {celsius_fahrenheit}")


async def setup(bot):
    await bot.add_cog(Converter(bot))
    print("Loaded Converter extension")
