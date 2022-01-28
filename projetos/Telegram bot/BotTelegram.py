from main.system.BuiltIn import LoadJson, SaveJson, Log, Start, Stop, ClearCache, LoadFunctions
from time import sleep

data = LoadJson("main/system/Config.json")
data["bot_on"] = True
SaveJson("main/system/Config.json", data)
for func_name, func in LoadFunctions("main/functions").items():
  globals()[func_name] = func
  is_avaliable = True
import os, traceback, telebot, requests
try:
  is_avaliable 
  Log("Funções disponíveis")
except NameError:
  is_avaliable = False 
  print("Funções não disponíveis")
  Log("Funções não disponíveis", None, 1)
auth = LoadJson("main/system/Auth.json")
bot = telebot.TeleBot(auth["TOKEN"])
connection_attempts = 0
no_command = False

@bot.message_handler(content_types = ["text", "audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact", "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo", "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id", "migrate_from_chat_id", "pinned_message"])
@bot.message_handler(chat_types = ["group", "supergroup", "private"])
def Filter(message):
  global connection_attempts, no_command
  connection_attempts = 0
  data = LoadJson("main/system/Config.json")
  functions = data["functions"]
  Log("Mensagem recebida", {"conteúdo": message}, 0)
  if message.chat.type in ["supergroup", "group"]:
    if message.text == "/start":
      Start(bot, message)
    elif message.text == "/stop" or message.content_type == "left_chat_member":
      Stop(bot, message)
    elif message.chat.id in data["group_list"]:
      command_sent = str(message.text) if message.caption == None else str(message.caption) 
      if len(command_sent) > 1 and len(command_sent) <= 50:
        if is_avaliable:
          command_sent += " "
          command_sent = command_sent[:command_sent.index(" ")].replace(f"@{bot.get_me().username}", "").lower().strip()
          adm_list = [n.user.first_name for n in bot.get_chat_administrators(message.chat.id)]
          for function, values in functions.items():
            if type(values) != list:
              triggers_list = [n.split("&") for n in values["triggers"]]
              for command in triggers_list:
                try:
                  if command[0] == "c":
                    if command_sent[0] == "/" and command_sent[1:] == command[1]:
                      Log("Comando ativou uma função", {"conteúdo": message, "comando": command_sent})
                      bot.send_chat_action(message.chat.id, "typing") 
                      if values["permission"] == 0:
                        if data["bot_on"]:
                          data = globals()[function](bot, message, data) 
                      elif values["permission"] == 1:
                        if message.from_user.first_name in adm_list:
                          data = globals()[function](bot, message, data)
                        else:
                          bot.reply_to(message, "\n".join(data["messages"]["without_permission_message"])) 
                      elif values["permission"] == 2:
                        if message.from_user.username == auth["CREATOR"]:
                          data = globals()[function](bot, message, data)
                        else:
                          bot.reply_to(message, "\n".join(data["messages"]["without_permission_message"])) 
                      if data != None:
                        SaveJson("main/system/Config.json", data)
                      Log("Função executada com sucesso", {"conteúdo": message, "comando": command_sent})
                      break
                  elif command[0] == "e":
                    if command[1] == message.content_type:
                      Log("Evento ativou uma função", {"conteúdo": message, "comando": command_sent})
                      data = globals()[function](bot, message, data)
                      if data != None:
                        SaveJson("main/system/Config.json", data)
                      break 
                  elif command[0] == "a":
                    bot.send_chat_action(message.chat.id, "typing")
                    data = globals()[function](bot, message, data)
                    no_command = True
                    if data != None:
                      SaveJson("main/system/Config.json", data)
                  elif command[0] == "w":
                    if command_sent == command[1]:
                      bot.send_chat_action(message.chat.id, "typing")
                      data = globals()[function](bot, message, data)
                      if data != None:
                        SaveJson("main/system/Config.json", data)
                      break
                except Exception:
                  Log("Função executada com erro", {"conteúdo": message, "comando": command_sent, "tipo": command[1]}, 2)
                  error = data["messages"]["error_message"].copy()
                  error.append(f"Exceção:\n\n\n\n{traceback.format_exc()}")
                  bot.reply_to(message, "\n".join(error))
                  break
              else:
                continue
              Log("Cache das funções limpo")
              ClearCache()
              break
          else:
            Log("Função não reconhecida", {"conteúdo": message, "comando": command_sent}, 1)
            if command_sent[0] == "/" and message.text not in ["/start", "/stop"] and no_command == False:
              bot.reply_to(message, "\n".join(data["messages"]["unknown_function_message"])) 
              Log("Comando desconhecido", {"comando": command_sent})
            else:
              no_command = False
        else:
          Log("Tentativa de ativação de uma função", {"comando": command_sent})
          bot.reply_to(message, "Nao há funções definidas nesse bot")
  elif message.chat.type == "private":
    pass

if __name__ == "__main__":
  for folder in ["main/functions", "main/system/cache"]:
    if not os.path.exists(folder):
      os.mkdir(folder)
  Log("Bot iniciado")
  print("\033[32mBot iniciado\033[0;0m")
  while True:
    try:
      Log("Loop do bot iniciado")
      bot.polling(interval = 0, skip_pending = True, non_stop = True)
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
      if data["keep_bot_on"]:
        print("Tentando conectar...")
        sleep(10)
      else:
        connection_attempts += 1
        print(f"Tentando conectar... {connection_attempts} tentativas")
        sleep(0.5)
      Log("Conexão perdida", flag = 1)
      if connection_attempts >= 30:
        Log("Conexão abortada", flag = 1)
        print("Não foi possível se conectar")
        Log("Bot encerrado com sucesso")
        print("Bot encerrado com sucesso")
        break
    except Exception as e:
      Log("Algum erro ocorreu no módulo principal", {"erro": traceback.format_exc()}, 2)
      print(traceback.format_exc())
      Log("Bot encerrado com falhas", {"erro": traceback.format_exc(), "motivo": e}, 2) 
      break
    else:
      Log("Bot encerrado com sucesso")
      print("Bot encerrado com sucesso")
      break
