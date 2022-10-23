#EnDa CAPP's structed module

#Import needed modules
import os

def installModule(module):
    command = "pip3 install " + str(module)
    if os.name in ("dos","nt"):
        command = "pip install " + str(module)
    os.system(command)

def verifyModules():
    try:
        from colorama import Fore
    except:
        print("The module 'COLORAMA' is not installed!")
        installModule("colorama")

    try:
        from pystyle import Colors,Colorate
    except:
        print("The module 'PYSTYLE' is not installed!")
        installModule("pystyle")
    
    try:
        import os
    except:
        print("The module 'OS' is corupted!")
        raise ModuleNotFoundError("Module 'OS' not found Error!")

    try:
        import random
    except:
        print("The module 'RANDOM' is corupted!") 
        raise ModuleNotFoundError("Module 'RANDOM' not found Error!")

#List of all needed modules
from colorama import Fore
import random
import os
from pystyle import Colors,Colorate