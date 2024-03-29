import discord
from datetime import datetime
from discord.ext import commands
from dotenv import dotenv_values
import asyncio
from commands.manager import Manager

# dotenv variables
config = dotenv_values(".env")
CLIENT_ID = config["CLIENT_ID"]
TOKEN = config["TOKEN"]
SERVER_ID = config["SERVER_ID"]

# intents
intents = discord.Intents.default()
intents.message_content = True

# class
manager = Manager()

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
    print(message)
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

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    try:
        channels = message.guild.channels
        for channel in channels:
            if channel.name == "🐦┇avisos":
                channelreply = channel
    except:
        print("Canal privado ---", message)
        channelreply = message.channel

    if message.content.startswith("!noclasstomorrow"):
        if manager.checkAutor(message):
            reply = manager.noClassTomorrow(message)
            await channelreply.send(reply)
        else:
            await message.channel.send("Você não pode realizar essa ação")
    elif message.content.startswith("!aviso"):
        if manager.checkAutor(message):
            reply = manager.shareMessage(message)
            await channelreply.send(reply)
        else:
            await message.channel.send("Você não pode realizar essa ação")
    elif message.content.startswith("!newtask"):
        if manager.checkAutor(message):
            reply = manager.newTask(message)
            await channelreply.send(reply)
        else:
            await message.channel.send("Você não pode realizar essa ação")
    elif message.content.startswith("!github"):
        reply = manager.github
        await message.channel.send(reply)
    elif message.content.startswith("!monitoria"):
        reply = manager.monitoria(message)
        await message.channel.send(reply)
    elif message.content.startswith("!anderson"):
        reply = manager.anderson()
        await message.channel.send(reply)
    elif message.content.startswith("!help"):
        reply = manager.help()
        await message.channel.send(reply)
    elif message.content.startswith("!f5"):
        if manager.checkAutor(message):
            reply = manager.atualizacao()
            await channelreply.send(reply)
        else:
            await message.channel.send("Você não pode realizar essa ação")
    elif message.content.startswith("!provas"):
        reply = manager.nextTests()
        await message.channel.send(reply)
    elif message.content.startswith("!avprovas"):
        if manager.checkAutor(message):
            reply = manager.nextTests()
            await channelreply.send(reply)
        else:
            await message.channel.send("Você não pode realizar essa ação")

client.run(TOKEN)