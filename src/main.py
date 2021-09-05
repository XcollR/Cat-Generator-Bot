import discord
import os
from keep_alive import keep_alive
from functions import *

client = discord.Client()


#############################################    MAIN    ####################################################


@client.event
async def on_ready():
  print("Connected!")  

@client.event
async def on_message(message):
  if message.content.startswith(";category"):
    await cat_category(client, message)

  elif message.content.startswith(";i"):
    await message.channel.send(welcome_text)

  elif message.content.startswith(";cat"):
    await get_cat(client, message)

  elif message.content.startswith(";gif"):
    await get_cat_gif(client, message)

    
keep_alive()
client.run(os.environ['TOKEN'])



