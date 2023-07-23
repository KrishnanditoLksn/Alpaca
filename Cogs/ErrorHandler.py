from discord.ext import commands
import discord


class HandleError(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot

    # ERROR
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send("Member not found !!")


async def setup(bot: commands.Bot):
    await bot.add_cog(HandleError(bot))
