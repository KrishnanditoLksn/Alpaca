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
    async def okeSip(self, ctx):
        message = await ctx.send("yo")
        emoji = '\N{THUMBS UP SIGN}'
        await message.add_reaction(emoji)


async def setup(bot: commands.Bot):
    await bot.add_cog(MemberEmojiReaction(bot))
