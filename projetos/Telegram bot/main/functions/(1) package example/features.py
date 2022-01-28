from urllib.parse import quote 
from bs4 import BeautifulSoup 
from random import randint 
import requests

def Echo(bot, message, data):
  bot.reply_to(message, message.text)
  data["keep_bot_on"] = False
  return data

def GetImage(bot, message, data):
  search = quote(message.text[message.text.index(" ") + 1:]) 
  link = f"https://www.google.com/search?q={search}&client=ms&tbm=isch"
  request = requests.get(link)
  soup = BeautifulSoup(request.content, "html.parser")
  images = [n.get("src").replace("&amp;s", "") for n in soup.find_all("img", {"class": "yWs4tf"})]
  image = requests.get(images[randint(0, len(images) - 1)])
  with open("main/system/cache/image.png", "wb") as a:
    a.write(image.content)
  with open("main/system/cache/image.png", "rb") as a:
    bot.send_photo(message.chat.id, a.read())
