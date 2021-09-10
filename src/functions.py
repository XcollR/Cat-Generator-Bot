import requests
import asyncio
import random

#WELCOME TEXT USED WHEN ;i is invoked.
welcome_text = "Hi, welcome to the Miau Bot! The purpose of this bot is to cheer you up or just to have some fun while looking at the different cats.\n\n**To use this bot:**\n - ;i To show the instructions.\n - ;cat To show a picture of a cat. \n - ;gif To show a cat gif. \n - ;category To select a specific cat category.\n\nBelow the images, you'll find some reactions:\n - 🐈: Gives some cat texts :)\n - 📌: Pins the image to the channel where you are using the bot.\n - 📷: Generates a cat gif.\n - ⏭️: Generates another cat image.\n\nEnjoy!!"

# TYPES OF MIAU
miau_type = ["miaaau", "miauu", "miaumiauu", "miaau", "meowwww", "miiauuu",
             "mmeoww", "mimiau", "meooow", "meowmeow", "meow", "mow",
             "mrow", "mrrr", "prr", "prrt", "hh", "mrrrrrrrrrrawr", "mew",
             "rrrr", "awr", "mEEEwr", "* yawns *", "* dances *"]

###################################    FUNCTIONS   ####################################################



#### GET A CATEGORY CAT FUNCTION ####
async def cat_category(message,client):
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
      msg = await message.channel.send(image_json[0]["url"])
      await msg.add_reaction("🐈" )
      await msg.add_reaction("📌")
      await msg.add_reaction("📷")
      await msg.add_reaction("⏭️")

    else:
      await message.channel.send("Sorry the category you choose doesn't exist :(")
     
  except asyncio.TimeoutError:
    await message.channel.send("Sorry, you took too long to choose a category :(")

  return
  
#### GET A RANDOM CAT FUNCTION ####

async def get_cat(message):
  image_json = requests.get("https://api.thecatapi.com/v1/images/search?mime_types=jpg,png")
  image_json = image_json.json()
  msg = await message.channel.send(image_json[0]["url"])
  await msg.add_reaction("🐈" )
  await msg.add_reaction("📌")
  await msg.add_reaction("📷")
  await msg.add_reaction("⏭️")


#### GET A RANDOM CAT GIF FUNCTION ####

async def get_cat_gif(message):
  image_json = requests.get("https://api.thecatapi.com/v1/images/search?mime_types=gif")
  image_json = image_json.json()
  msg = await message.channel.send(image_json[0]["url"])
  await msg.add_reaction("🐈" )
  await msg.add_reaction("📌")
  await msg.add_reaction("📷")
  await msg.add_reaction("⏭️")


### MANAGE REACTIONS ###

async def manage_reactions(reaction, user, client):
  message = reaction.message
  channel = reaction.message.channel
  if reaction.message.author == client.user:
    if reaction.emoji == "⏭️" and reaction.count > 1:
      await get_cat(message)
    if reaction.emoji == "📌":
      if reaction.count == 2:
        await message.pin()
      elif reaction.count >= 3:
        await channel.send("Picture already pinned :)")
    if reaction.emoji == "🐈" and reaction.count > 1:
      text = get_miau_text()
      await channel.send(text)
    if reaction.emoji == "📷" and reaction.count > 1:
      await get_cat_gif(message)



#### GET A RANDOM MEOW TYPE ####

def get_miau_text():
  text = ""
  for x in range(random.randint(1,5)):
    text += random.choice(miau_type) + " "
  return text

