import discord
import os
import commands as commands
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print('IT\'S ALIVE!!!!!!!!!!!!!!!!!!!!')

@client.event
async def on_message(message):

    # Stops the bot from replying to it's own messages
    if message.author == client.user:
        return

    await commands.user_commands(message)

keep_alive()

client.run(os.getenv('TOKEN'))
