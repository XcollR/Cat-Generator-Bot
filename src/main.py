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
  message.content = message.content.lower()
  if message.content.startswith(";category"):
    await cat_category(message)

  elif message.content.startswith(";i"):
    await message.channel.send(welcome_text)

  elif message.content.startswith(";cat"):
    await get_cat(message)

  elif message.content.startswith(";gif"):
    await get_cat_gif(message)

@client.event
async def on_reaction_add(reaction, user):
  await manage_reactions(reaction, user, client)
    

    
keep_alive()
client.run(os.environ['TOKEN'])

