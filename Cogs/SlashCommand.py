import discord
from discord import app_commands


class HelpCommands(app_commands.Group):

    @app_commands.command(name="command-1")
    async def my_command(self, interaction: discord.Interaction) -> None:
        """ /command-1 """
        await interaction.response.send_message("Hello from command 1!", ephemeral=True)

    @app_commands.command()
    async def pong(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"pong")


async def setup(bot):
    bot.tree.add_command(HelpCommands(name="test", description="test slash"))
    print("Loaded core information extension")
