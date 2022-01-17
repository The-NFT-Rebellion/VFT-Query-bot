import discord
import random

command_prefix = ";"

async def user_commands(message):
    if message.content == command_prefix + "test":
        await message.channel.send("yo!")

    #if message.content == command_prefix + "fella":
    #  await message.channel.send(file=discord.File('images/fella.webp'))