from sys import executable
from subprocess import check_call
from os import chdir 

chdir("/storage/emulated/0/Android/data/io.spck.editor.node/files")
check_call([executable, "-m", "http.server", "8000"])
