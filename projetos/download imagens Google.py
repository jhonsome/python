import requests, lxml 
from bs4 import BeautifulSoup 
from random import randint 
from urllib.parse import quote

pesquisa = quote("Boeing 787".strip()) 
link = f"https://www.google.com/search?q={pesquisa}&client=ms&tbm=isch"
resposta = requests.get(link)
sopa = BeautifulSoup(resposta.content, "lxml")
imglist = [n.get("src").replace("&amp;s", "") for n in sopa.find_all("img", {"class": "yWs4tf"})]
img = requests.get(imglist[randint(0, len(imglist) - 1)])

with open("/sdcard/imagem.png", "wb") as a:
  a.write(img.content)
