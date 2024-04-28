from discord.ext import commands
import discord


class HandleError(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot
        self.error_messages = {
            commands.MemberNotFound: "Member not found !!",
            commands.MissingRequiredArgument: "Missing parameter Input !!!",
            commands.CommandInvokeError: "Object has no attribute send",
            commands.NotOwner: "You are not owner of this bot !!!",
            commands.UserInputError: "Input error !!",
            commands.CommandNotFound: "Command not found !!",
            commands.CommandOnCooldown: "Command on cooldown !!"
        }

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if error.__class__ in self.error_messages:
            await ctx.send(self.error_messages[error.__class__])


async def setup(bot: commands.Bot):
    await bot.add_cog(HandleError(bot))
    print("Loaded Global error handler extension")
