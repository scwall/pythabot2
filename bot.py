import discord
import json
from discord.ext import commands


def keys(file, key):
    with open(file) as k:
        data = json.load(k)
        return data['token']


TOKEN = keys('key.json', 'token')

description = '''pythabot in Python'''
bot = commands.Bot(command_prefix='?', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def hello():
    """Says world"""
    await bot.say("world")


@bot.command()
async def add(left: int, right: int):
    """Adds two numbers together."""
    await bot.say(left + right)


bot.run(TOKEN)
