import asyncio
import os
import discord.ext.tasks
from discord.ext import commands
import random
import dotenv

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), case_insensitive=True)
intents = discord.Intents.all()
client = discord.Client(intents=intents)

dotenv.load_dotenv(dotenv.find_dotenv("Alpacaa/load_dotenv.env"))
TOKEN = os.getenv("DISCORD_TOKEN")


@bot.event
async def on_ready():
    print('===================')
    print(f'Logged in as {bot.user}')
    print('===================')

    try:
        for filename in os.listdir("./Cogs"):
            if filename.endswith(".py"):
                await bot.load_extension(f"Cogs.{filename[:-3]}")
    except Exception:
        print("Could not load cogs as extension")


@bot.command(aliases=['p'])
async def ping(ctx):
    await ctx.send("Apa cok")


def run():
    @bot.command(aliases=['h'])
    async def hello(ctx):
        await ctx.send(f"Hello cok {client.user.mention}")

    @bot.command()
    async def repeated(ctx, times: int):
        content = "im looping!!"
        for i in range(times):
            await ctx.send(content)


bot.run(os.environ.get("DISCORD_TOKEN"))

if __name__ == "__main__":
    run()
