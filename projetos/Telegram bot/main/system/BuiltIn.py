from datetime import datetime 
from subprocess import check_call 
from importlib import import_module
from inspect import getmembers, isfunction 
from base64 import b64encode, b64decode 
import json, os, sys, shutil 

def Log(text, params = None, flag = 0):
  data = LoadJson("main/system/Config.json")
  if data["debug_mode_on"]:
    params_text = ""
    if flag == 0:
      type = "INFORMAÇÃO"
    elif flag == 1:
      type = "ALERTA"
    elif flag == 2:
      type = "ERRO"
    if params != None:
      for key, value in params.items():
        params_text += f"{key}: {value}, "
    if not os.path.exists("main/Debug.log"):
      with open("main/Debug.log", "w") as a:
        date = datetime.now()
        a.write(f"== 'INFORMAÇÃO' {date.day}/{date.month}/{date.year} {date.hour}:{date.minute}:{date.second} - Registro iniciado. ==\n")
    with open("main/Debug.log", "a") as a:
      date = datetime.now()
      a.write(f"== '{type}' {date.day}/{date.month}/{date.year} {date.hour}:{date.minute}:{date.second} - {text}. {params_text} ==\n")

def ClearCache():
  for trash in os.listdir("main/system/cache"):
    if os.path.isdir(f"main/system/cache/{trash}"):
      shutil.rmtree(f"main/system/cache/{trash}")
    else:
      os.remove(f"main/system/cache/{trash}")

def SaveJson(path, dictionary):
  with open(path, "w", encoding = "utf-8") as a:
    a.write(json.dumps(dictionary, indent = 2, ensure_ascii = False)) 

def LoadJson(path):
  with open(path, "r", encoding = "utf-8") as a:
    data = json.loads(a.read())
  return data

def MergeJson(json1, json2, _type = dict):
  if _type == dict:
    for key, value in json2.items():
      if type(value) == list or type(value) == dict:
        try:
          json1[key]
        except KeyError:
          json1[key] = value
        else:
          MergeJson(json1[key], json2[key], list if type(value) == list else dict)
      else:
        json1[key] = value 
  elif _type == list:
    for value in json2:
      if not value in json1:
        json1.append(value)
  return json1

def Start(bot, message):
  data = LoadJson("main/system/Config.json")
  if message.from_user.username == data["creator"]:
    if not message.chat.id in data["group_list"]:
      data["group_list"].append(message.chat.id)
      bot.reply_to(message, "Bot recebendo comandos desse grupo") 
  SaveJson("main/system/Config.json", data)
  
def Stop(bot, message):
  data = LoadJson("main/system/Config.json")
  if message.content_type == "left_chat_member" and message.left_chat_member.username == bot.get_me().username:
    if message.chat.id in data["group_list"]:
      data["group_list"].remove(message.chat.id)
  else:
    if message.chat.id in data["group_list"]:
      data["group_list"].remove(message.chat.id)
      bot.reply_to(message, "Bot encerrado para esse grupo")
  SaveJson("main/system/Config.json", data)

#def GetMedia(bot, file_id):
#  file_info = bot.get_file(file_id)
#  return (bot.download_file(file_info.file_path), file_info.file_path[file_info.file_path.index("/") + 1:])

#def GetArgs(message, need_args = True):
#  message_text = m.text if not m.text == None else m.caption
#  if message_text.count(" ") > 0:
#    command, args = message_text.split(sep = " ", maxsplit = 1)
#    message_text = f"{command} {message.reply_to_message.text}; {args}" if message.reply_to_message != None else message_text
#  else:
#    command = message_text.split(sep = " ", maxsplit = 1)[0]
#    message_text = f"{command} {message.reply_to_message.text}" if message.reply_to_message != None else None
#  try:
#    return [n.strip() for n in message_text[message_text.index(" "):].split(";")]
#  except (ValueError, AttributeError):
#    if need_args:
#      raise Exception("\n\nEssa função necessita de alguns argumentos")
#    else:
#      return []

def InstallLibs(dict_libraries, directory = None):
  if directory != None:
    if not os.path.exists(directory):
      os.mkdir(directory)
    sys.path.append(directory)
  for import_name, lib_name in dict_libraries.items():
    attempts = 0
    while True:
      try:
        if directory == None:
          globals()[import_name] = import_module(import_name)
        else:
          globals()[import_name] = import_module(f"{directory.replace('/', '.')}.{import_name}", directory)
        break
      except ModuleNotFoundError:
        attempts += 1
        if attempts == 2:
          raise Exception(f"Module not found: {lib_name}")
        if directory == None:
          check_call([sys.executable, "-m", "pip", "install", "--upgrade", lib_name])
        else:
          check_call([sys.executable, "-m", "pip", "install", f"--target={directory}", "--upgrade", lib_name])

def LoadFunctions(path):
  loaded_functions = dict() 
  functions_list = list()
  index = 1
  for package in os.listdir(path):
    if package[0] != "(":
      if os.path.exists(f"{path}/{package}/features.py") and os.path.exists(f"{path}/{package}/Config.json"):
        os.rename(f"{path}/{package}", f"{path}/({index}) {package}")
        index += 1
  packages = os.listdir(path)
  packages.sort()
  for package in packages:
    if os.path.exists(f"{path}/{package}/features.py") and os.path.exists(f"{path}/{package}/Config.json"):
      data = LoadJson("main/system/Config.json")
      json_package = LoadJson(f"{path}/{package}/Config.json")
      try:
        json_package["functions"]
      except KeyError:
        pass
      else:
        for func in json_package["functions"]:
          data["functions"][func] = func
        del json_package["functions"]
      data = MergeJson(data, json_package)
      InstallLibs(data["dependencies"], "main/libraries")
      mod = import_module(f"main.functions.{package}.features")
      for function in getmembers(mod, isfunction):
        loaded_functions[function[0]] = function[1]
  for t in data["functions"]:
    if type(t) != list:
      if not t in loaded_functions.keys():
        del data["functions"][t]
  SaveJson("main/system/Config.json", data)
  return loaded_functions
