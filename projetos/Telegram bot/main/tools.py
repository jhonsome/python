import json 
import os
import sys
import importlib

def CreateDirectories(directory_list):
  for directory in directory_list:
    if not os.path.exists(directory):
      os.mkdir(directory)

def InstallDependencies(dependency_list):
  try:
    for module in dependency_list:
      globals()[module[1]] = importlib.import_module(module[1])
  except ModuleNotFoundError:
    install_list = map(lambda )
    check_call([sys.executable, "-m", "pip", "install", "--target=main/dependencies", "--upgrade"] + map())
    globals()["telebot"] = importlib.import_module("telebot")
  

def SaveJson(json):
  json.dumps(json, indent = 2, ensure_ascii = False)

def LoadJson(path):
  return json.load(path)
