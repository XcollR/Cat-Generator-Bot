import discord
import os
import json
import requests
import asyncio
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print("Connected!")  

@client.event
async def on_message(message):
  if message.content.startswith(";category"):
    text = ""
    await message.channel.send("Select one of these categories and write it down:")
    categories = requests.get("https://api.thecatapi.com/v1/categories")
    categories = categories.json()
    for categs in categories:
      text = text + categs["name"] + "\n"
    await message.channel.send(text)

    try:
      msg = await client.wait_for('message', timeout=15)    
      categ = msg.content
      categories = requests.get("https://api.thecatapi.com/v1/categories")
      categories = categories.json()
      id_category = ""
      found = 0
      for x in categories:
        if x["name"] == categ:
          id_category = str(x["id"])
          found = 1

      if found == 1:
          url = "https://api.thecatapi.com/v1/images/search?category_ids=" + id_category
          image_json = requests.get(url)
          image_json = image_json.json()
          await message.channel.send(image_json[0]["url"])
      else:
        await message.channel.send("Sorry the category you chose doesn't exist :(")
     
    except asyncio.TimeoutError:
      await message.channel.send("Sorry, you took too long to choose a category :(")

    


  elif message.content.startswith(";i"):
    await message.channel.send("Hi, welcome to the Miau Bot! The purpose of this bot is to cheer you up or just to have some fun while looking at the different cats.\nTo use this bot:\n - ;i To show the instructions.\n - ;cat To show a picture of a cat. \n - ;gif To show a cat gif. \nEnjoy!")

  elif message.content.startswith(";cat"):
    image_json = requests.get("https://api.thecatapi.com/v1/images/search?mime_types=jpg,png")
    image_json = image_json.json()
    await message.channel.send(image_json[0]["url"])

  elif message.content.startswith(";gif"):
    image_json = requests.get("https://api.thecatapi.com/v1/images/search?mime_types=gif")
    image_json = image_json.json()
    await message.channel.send(image_json[0]["url"])    
    
keep_alive()
client.run(os.environ['TOKEN'])
