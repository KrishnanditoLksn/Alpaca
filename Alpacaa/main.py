import dotenv
import discord
import os

dotenv.load_dotenv(dotenv.find_dotenv('load_dotenv.env'))
TOKEN = os.getenv('DISCORD_TOKEN')


class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged in as ', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            print(f'Logged in as {message.author} : {message.content}')
            return

        if message.content == 'ping':
            await message.channel.send('pong')

        elif message.content == 'hello':
            await message.channel.send('helloww')


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)
