from discord.ext import commands

from main import bot


@bot.command()
async def github(ctx):
    await ctx.send('https://github.com/gustapavao/btico')

