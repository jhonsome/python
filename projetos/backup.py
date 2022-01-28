import os, zipfile
from datetime import datetime

raiz = "/sdcard"
dirsIgnorados = ["/sdcard/Android", "/sdcard/backup"]
dirs = [n if n not in dirsIgnorados else "" for n in os.listdir(raiz)]
nomeDoDispositivo = "Moto e6 Play"
data = datetime.now()
filepath = f"backup/{nomeDoDispositivo} backup {data.day}-{data.month}-{data.year}-{data.hour}-{data.minute}-{data.second}"

if not os.path.exists(os.path.join(raiz, "backup")):
  os.mkdir(os.path.join(raiz, "backup"))
os.chdir(raiz)
for root, dirs, files in os.walk(raiz):
  
    with zipfile.ZipFile(filepath, "a") as zp:
      for arquivo in files:
        if not f"{root}/{arquivo}" in dirsIgnorados:
        print(f"Compactando: {f'{root}/{arquivo}'}")
        zp.write(f"{root}/{arquivo}")
os.rename(filepath, filepath + ".zip")
print("\n--Finalizado--")
