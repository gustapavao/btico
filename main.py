import discord
from dotenv import dotenv_values

config = dotenv_values(".env")
CLIENT_ID = config["CLIENT_ID"]
TOKEN = config["TOKEN"]
SERVER_ID = config["SERVER_ID"]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('ping'):
        await message.channel.send('pong')

client.run(TOKEN)
