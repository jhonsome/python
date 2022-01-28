from gtts import gTTS

texto = "Olá, tudo bem?"
língua = "pt-br"
path = "audio.mp3"

fala = gTTS(text = texto, lang = língua, slow = False)
fala.save(path)
