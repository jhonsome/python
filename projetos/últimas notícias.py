import requests, lxml
from bs4 import BeautifulSoup 
from urllib.parse import quote 

src = quote("últimas notícias")
url = f"https://www.google.com/search?q={src}&sourceid=chrome"
resposta = requests.get(url)
sopa = BeautifulSoup(resposta.content, "lxml")
notícias = list()
principal = sopa.find("span", {"class": "atOwb UMOHqf"})
títulos = sopa.find_all("span", {"class": "UMOHqf EDgFbc"})
fontes = sopa.find_all("span", {"class": "UMOHqf VbKY9d"})
links = sopa.find_all("a", {"class": "tHmfQe"})
for t in range(len(títulos)):
  notícias.append([títulos[t].string, fontes[t].string, links[t].get("href").replace("/url?q=", "")])

print(f"""
{principal.string}

-------------

{notícias[0][0]}

{notícias[0][2]}
fonte: {notícias[0][1]}

-------------

{notícias[1][0]}

{notícias[1][2]}
fonte: {notícias[1][1]}

-------------

{notícias[2][0]}

{notícias[2][2]}
fonte: {notícias[2][1]}

-------------
""")
