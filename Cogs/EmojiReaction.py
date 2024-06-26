from discord.ext import commands


class MemberEmojiReaction(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.guild_only()
    async def greetings(self, ctx, member):
        guild = member.guild

        if guild.system.channel is not None:
            await ctx.send(f"Hellow {member.mention},"
                           f"Welcome to {guild.name}")

    @commands.command(aliases=['ok'])
    async def oke_sip(self, ctx):
        message = await ctx.send("yo")
        emoji = '\N{THUMBS UP SIGN}'
        await message.add_reaction(emoji)

    @commands.command(aliases=['sad'])
    async def sad_member(self, ctx):
        message = await ctx.send("Dont be sad bro !!!")
        sad_emoji = "🙁"
        await message.add_reaction(sad_emoji)

    @commands.command(aliases=['hepi'])
    async def happy_member(self, ctx):
        message = await ctx.send("Eurekaaaa")
        happy_emoji = "😊"
        await message.add_reaction(happy_emoji)


async def setup(bot: commands.Bot):
    await bot.add_cog(MemberEmojiReaction(bot))
