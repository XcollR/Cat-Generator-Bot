import requests
import asyncio

#WELCOME TEXT USED WHEN ;i is invoked.
welcome_text = "Hi, welcome to the Miau Bot! The purpose of this bot is to cheer you up or just to have some fun while looking at the different cats.\nTo use this bot:\n - ;i To show the instructions.\n - ;cat To show a picture of a cat. \n - ;gif To show a cat gif. \n - ;category: To select a specific cat category.\nEnjoy!"

###################################    FUNCTIONS     ########################################################

#### GET A CATEGORY CAT FUNCTION ####
async def cat_category(client, message):
  text = ""
  await message.channel.send("**Select one of these categories and write it down:**")
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
      await message.channel.send("Sorry the category you choose doesn't exist :(")
     
  except asyncio.TimeoutError:
    await message.channel.send("Sorry, you took too long to choose a category :(")

  return
  
#### GET A RANDOM CAT FUNCTION ####

async def get_cat(client, message):
  image_json = requests.get("https://api.thecatapi.com/v1/images/search?mime_types=jpg,png")
  image_json = image_json.json()
  await message.channel.send(image_json[0]["url"])
  #await message.add_reaction("🐈")
  #await send_reactions(message)

#### GET A RANDOM CAT GIF FUNCTION ####

async def get_cat_gif(client, message):
  image_json = requests.get("https://api.thecatapi.com/v1/images/search?mime_types=gif")
  image_json = image_json.json()
  await message.channel.send(image_json[0]["url"]) 


#### SEND REACTIONS ####

async def send_reactions(message):
  channel_name = message.channel.name
  print(channel_name)
