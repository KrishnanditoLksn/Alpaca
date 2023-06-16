import dotenv
import discord
import os
from discord.ext import commands
import datetime
import discord.ext.tasks

dotenv.load_dotenv(dotenv.find_dotenv('load_dotenv.env'))
TOKEN = os.getenv('DISCORD_TOKEN')


# id = 981881633932189716

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged in as ', self.user)

    async def on_message(self, message):
        client.get_guild(981881633932189716)
        channels = ["bot_test_room"]
        if message.author == self.user:
            print(f'Hello world im a bot {message.author} : {message.content}')
            return

        if message.content == 'ping':
            await message.channel.send('pong')

        elif message.content == 'hello':
            await message.channel.send('helloww')

        if str(message.channel in channels):
            if message.content.find("!halo") != 1:
                await message.channel.send("Haii")


class BanFriend(commands.FlagConverter):
    member: discord.Member
    reason: str
    days: int = 1


@commands.command()
async def ban(ctx, *, flags: BanFriend):
    plural = f'{flags.days} days' if flags.days != 1 else f'{flags.days} day'
    await ctx.send(f'Banned {flags.member} for {flags.reason!r} (deleted {plural} worth of messages)')


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)
