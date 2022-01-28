import requests 

url = "https://github.com/yourkin/fileupload-fastapi/raw/a85a697cab2f887780b3278059a0dd52847d80f3/tests/data/test-10mb.bin"
filename = url.split('/')[-1]
header = requests.head(url, allow_redirects = True).headers
conteúdo = header.get('content-type').lower()
if "text" in conteúdo or "html" in conteúdo:
  raise Exception("Não é um arquivo de mídia")
with requests.get(url, stream = True) as r:
  with open(filename, 'wb') as f:
    for chunk in r.iter_content(chunk_size = 1024): 
      f.write(chunk)
