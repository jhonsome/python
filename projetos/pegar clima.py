import requests, lxml 
from urllib.parse import quote 
from bs4 import BeautifulSoup 

local = "juazeiro do norte"
url = f"https://www.google.com/search?q=clima+{quote(local)}"
resposta = requests.get(url)
soup = BeautifulSoup(resposta.content, "lxml")
nome = soup.find_all("span", {"class": "BNeawe tAd8D AP7Wnd"})[0].string
temp = soup.find_all("div", {"class": "BNeawe iBp4i AP7Wnd"})[0].string
data, hora, cond = soup.find_all("div", {"class": "BNeawe tAd8D AP7Wnd"})[0].string.replace("\n", " ").split(" ", 2)
print(f"""
clima para {nome}

{temp}

{cond}
{data} {hora}""")
