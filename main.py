from commands.mentoria import Mentoria
from commands.tests import Tests

import discord
from discord import app_commands
from dotenv import dotenv_values

# dotenv variables
config = dotenv_values(".env")
CLIENT_ID = config["CLIENT_ID"]
TOKEN = config["TOKEN"]
SERVER_ID = config["SERVER_ID"]
MAIN_SERVER_ID = config["MAIN_SERVER_ID"]


MY_GUILD = discord.Object(id=MAIN_SERVER_ID)


class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


mentor = Mentoria()
client = MyClient()
tests = Tests()


@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')


@client.tree.command(description='Mentorias disponiveis.')
@app_commands.choices(choice=[
    app_commands.Choice(name="ME", value="me"),
    app_commands.Choice(name="GE", value="ge"),
    app_commands.Choice(name="Outra", value="petcc"),
])
async def mentoria(
        interaction: discord.Interaction,
        choice: str
):
    """Reply with the days and hours of mentors"""
    await interaction.response.send_message(f'{mentor.retmentoria(choice)}', ephemeral=True)


@client.tree.command(description='Próximas provas.')
async def provas(
        interaction: discord.Interaction
):
    """Reply with the next tests"""
    await interaction.response.send_message(f'{tests.all_tests()}', ephemeral=True)


@client.tree.command(description='Git do Bot.')
async def github(interaction: discord.Interaction):
    await interaction.response.send_message("Fique a vontade para contribuir:\nhttps://github.com/gustapavao/btico")


client.run(TOKEN)
