import discord
from datetime import datetime
from discord.ext import commands
from dotenv import dotenv_values


# dotenv variables
config = dotenv_values(".env")
CLIENT_ID = config["CLIENT_ID"]
TOKEN = config["TOKEN"]
SERVER_ID = config["SERVER_ID"]

# intents
intents = discord.Intents.default()
intents.message_content = True


# discord connection
client = discord.Client(intents=intents)

# defining the command prefix
bot = commands.Bot(command_prefix='/', intents=intents)


# login
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ping'):
        await message.channel.send('pong')

    if message.content.startswith("!github"):
        await message.channel.send('https://github.com/gustapavao/btico')

    if message.content.startswith("!hora"):
        hoje = datetime.now()
        hoje_string = hoje.strftime("%H:%M")
        await message.channel.send(f'Agora são {hoje_string} em ponto.')


# commands
@bot.command()
async def github(ctx):
    await ctx.send('https://github.com/gustapavao/btico')

client.run(TOKEN)
