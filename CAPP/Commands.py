#EnDa CAPP's commands file

#Import needed modules
try:
    import os
    from colorama import Fore
    from pystyle import Colors,Colorate
    import sys
    import time
    from pyfiglet import *
except:
    raise ModuleNotFoundError("Please install all needed modules!")

#Define an install function
def installModule(module):
    command = "pip3 install " + str(module)
    if os.name in ("dos","nt"):
        command = "pip install " + str(module)
    os.system(command)

#Define an command executor function
def commandExecutor(command):
    os.system(command)

#Define a variety of commands depends on operator system
def varietyCommandExecutor(other,windows):
    command = other
    if os.name in ("dos","nt"):
        command = windows
    os.system(command)