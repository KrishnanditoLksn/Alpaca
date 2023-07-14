import os
import discord.ext.tasks
from discord.ext import commands
import random
import dotenv

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())
intents = discord.Intents.all()
client = discord.Client(intents=intents)

dotenv.load_dotenv(dotenv.find_dotenv("load_dotenv.env"))
TOKEN = os.getenv("DISCORD_TOKEN")


@bot.event
async def on_ready():
    print('===================')
    print(f'Logged in as {bot.user}(ID : {bot.user.name}')
    print('===================')


@bot.command()
async def ping(ctx):
    await ctx.send("Apa cok")


@bot.command()
async def repeated(ctx, times: int):
    content = "njir loop"
    for i in range(times):
        await ctx.send(content)


bot.run(os.environ.get("DISCORD_TOKEN"))
