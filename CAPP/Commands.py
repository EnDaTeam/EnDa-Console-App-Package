#EnDa CAPP's commmands section

#import os module
import os

#Define an command executor
def commandexecutor(command):
    command = command
    os.system(command)

#Define an variety of command executor
def varietycommandexecutor(command1,command2):
    command = command1
    if os.name in ("dos","nt"):
        command = command2
    os.system(command)