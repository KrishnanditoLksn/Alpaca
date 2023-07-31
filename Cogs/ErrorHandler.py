from discord.ext import commands
import discord


class HandleError(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send("Member not found !!")

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing parameter Input !!!")

        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("Object has no attribute send")

        if isinstance(error, commands.NotOwner):
            await ctx.send("You are not owner of this bot !!!")

        if isinstance(error, commands.UserInputError):
            await ctx.send("Input error !!")


async def setup(bot: commands.Bot):
    await bot.add_cog(HandleError(bot))
    print("Loaded Global error handler extension")
