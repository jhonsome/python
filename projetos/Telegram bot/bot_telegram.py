import sys
import importlib 
from subprocess import check_call 
from main import tools

tools.CreateDirectories(["main/cache", "main/dependencies", "main/command_pack"])
sys.path.append("main/dependencies")

while True:
  pass
bot = telebot.TeleBot()
bot.infinity_polling()
