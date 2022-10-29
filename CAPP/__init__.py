#EnDa CAPP's main script

#Import needed modules
from .Commands import *
from .AsciiArt import *

#Define an space function (enter)
def enter(lines=1):
    for i in range(1):
        print("")

#Define an clear terminal function
def clearConsole():
    varietyCommandExecutor("clear","cls")

#Define a slow printing function
def slowPrint(text:str,times=0.2):
    for i in text + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(times)

#Define a custom command executor
def customCommandExecutor(command1,variety=0,command2=0):
    try:
        if variety:
            varietyCommandExecutor(command1,command2)
        else:
            commandExecutor(command1)
    except:
        raise ValueError("Something went wrong in Custom Command Executor! [ENDA CAPP]")

#Define an error output 
def error(text:str,option:int=0,slowprinting:bool=False):
    try:
        int(option)
    except:
        raise ValueError("The option from error function is not an integer! [ENDA CAPP]")
    if slowprinting:
        if int(option) == 1:
            slowprinting(Fore.RED + "[ERROR]" + Fore.WHITE + " >> " + Fore.LIGHTRED_EX + str(text) + Fore.RESET)
        elif int(option) == 2:
            slowPrint(Fore.RED + "ERROR" + Fore.WHITE + " >> " + Fore.LIGHTRED_EX + str(text) + Fore.RESET)
        elif int(option) == 3:
            slowPrint(Fore.RED + """       
    ▒█▀▀▀ █▀▀█ █▀▀█ █▀▀█ █▀▀█ 
    ▒█▀▀▀ █▄▄▀ █▄▄▀ █░░█ █▄▄▀ 
    ▒█▄▄▄ ▀░▀▀ ▀░▀▀ ▀▀▀▀ ▀░▀▀
            """ + Fore.LIGHTRED_EX)
            enter()
            slowPrint(str(text) + Fore.RESET) 
        elif int(option) == 4:
            slowPrint(Colorate.Horizontal(Colors.white_to_red,"""
        (    (        )   (     
        )\ ) )\ )  ( /(   )\ )  
    (   (()/((()/(  )\()) (()/(  
    )\   /(_))/(_))((_)\   /(_)) 
    ((_) (_)) (_))    ((_) (_))   
    | __|| _ \| _ \  / _ \ | _ \  
    | _| |   /|   / | (_) ||   /  
    |___||_|_\|_|_\  \___/ |_|_\                                                                  
        """,1 + Fore.LIGHTRED_EX))
            enter()
            slowPrint(str(text) + Fore.RESET) 
        elif int(option) == 5:
            slowPrint(Colorate.Horizontal(Colors.white_to_red,r"""
    ___ ___ ___  ___  ___ 
    | __| _ \ _ \/ _ \| _ \
    | _||   /   / (_) |   /
    |___|_|_\_|_\\___/|_|_\                                                          
        """, 1))
            enter()
            slowPrint(str(text) + Fore.RESET) 
    else:
        if int(option) == 1:
            print(Fore.RED + "[ERROR]" + Fore.WHITE + " >> " + Fore.LIGHTRED_EX + str(text) + Fore.RESET)
        elif int(option) == 2:
            print(Fore.RED + "ERROR" + Fore.WHITE + " >> " + Fore.LIGHTRED_EX + str(text) + Fore.RESET)
        elif int(option) == 3:
            print(Fore.RED + """       
    ▒█▀▀▀ █▀▀█ █▀▀█ █▀▀█ █▀▀█ 
    ▒█▀▀▀ █▄▄▀ █▄▄▀ █░░█ █▄▄▀ 
    ▒█▄▄▄ ▀░▀▀ ▀░▀▀ ▀▀▀▀ ▀░▀▀
            """ + Fore.LIGHTRED_EX)
            enter()
            print(str(text) + Fore.RESET)
        elif int(option) == 4:
            print(Colorate.Horizontal(Colors.white_to_red,"""
      (    (        )   (     
      )\ ) )\ )  ( /(   )\ )  
     (   (()/((()/(  )\()) (()/(  
     )\   /(_))/(_))((_)\   /(_)) 
    ((_) (_)) (_))    ((_) (_))   
    | __|| _ \| _ \  / _ \ | _ \  
    | _| |   /|   / | (_) ||   /  
    |___||_|_\|_|_\  \___/ |_|_\                                                                  
        """,1 + Fore.LIGHTRED_EX))
            enter()
            print(str(text) + Fore.RESET)
        elif int(option) == 5:
            print(Colorate.Horizontal(Colors.white_to_red,r"""
    ___ ___ ___  ___  ___ 
    | __| _ \ _ \/ _ \| _ \
    | _||   /   / (_) |   /
    |___|_|_\_|_\\___/|_|_\                                                          
        """, 1))
            enter()
            print(Fore.LIGHTRED_EX + str(text) + Fore.RESET)
    if int(option) not in (1,2,3,4,5):
        raise ValueError("The option from error function is not an integer (1,2,3,4,5) ! [ENDA CAPP]")

#Define a tip output
def tip(text:str,option:int=0,slowprinting:bool=False):
    try:
        int(option)
    except:
        raise ValueError("The option from tip function is not an integer (1,2,3,4,5) ! [ENDA CAPP]")
    if slowprinting:
        if int(option) == 1:
            slowprinting(Fore.LIGHTYELLOW_EX + "[TIP]" + Fore.WHITE + " >> " + Fore.LIGHTYELLOW_EX + str(text) + Fore.RESET)
        elif int(option) == 2:
            slowPrint(Fore.LIGHTYELLOW_EX + "TIP" + Fore.WHITE + " >> " + Fore.LIGHTYELLOW_EX + str(text) + Fore.RESET)
        elif int(option) == 3:
            slowPrint(Fore.LIGHTYELLOW_EX + """       
    ▀▀█▀▀ ▀█▀ ▒█▀▀█ 
    ░▒█░░ ▒█░ ▒█▄▄█ 
    ░▒█░░ ▄█▄ ▒█░░░
            """ + Fore.LIGHTYELLOW_EX)
            enter()
            slowPrint(str(text) + Fore.RESET) 
        elif int(option) == 4:
            slowPrint(Colorate.Horizontal(Colors.red_to_yellow,"""
            (    (     
      *   ) )\ ) )\ )  
    ` )  /((()/((()/(  
     ( )(_))/(_))/(_)) 
    (_(_())(_)) (_))   
    |_   _||_ _|| _ \  
      | |   | | |  _/  
      |_|  |___||_|                                                                   
        """,1 + Fore.LIGHTYELLOW_EX))
            enter()
            slowPrint(str(text) + Fore.RESET) 
        elif int(option) == 5:
            slowPrint(Colorate.Horizontal(Colors.yellow,r"""
      _____ ___ ___ 
     |_   _|_ _| _ \
       | |  | ||  _/
       |_| |___|_|                                                                    
        """, 1))
            enter()
            slowPrint(Fore.LIGHTYELLOW_EX + str(text) + Fore.RESET) 
    else:
        if int(option) == 1:
            print(Fore.LIGHTYELLOW_EX + "[TIP]" + Fore.WHITE + " >> " + Fore.LIGHTYELLOW_EX + str(text) + Fore.RESET)
        elif int(option) == 2:
            print(Fore.LIGHTYELLOW_EX + "TIP" + Fore.WHITE + " >> " + Fore.LIGHTYELLOW_EX + str(text) + Fore.RESET)
        elif int(option) == 3:
            print(Fore.LIGHTYELLOW_EX + """       
    ▀▀█▀▀ ▀█▀ ▒█▀▀█ 
    ░▒█░░ ▒█░ ▒█▄▄█ 
    ░▒█░░ ▄█▄ ▒█░░░
            """ + Fore.LIGHTYELLOW_EX)
            enter()
            print(str(text) + Fore.RESET) 
        elif int(option) == 4:
            print(Colorate.Horizontal(Colors.red_to_yellow,"""
            (    (     
      *   ) )\ ) )\ )  
    ` )  /((()/((()/(  
     ( )(_))/(_))/(_)) 
    (_(_())(_)) (_))   
    |_   _||_ _|| _ \  
      | |   | | |  _/  
      |_|  |___||_|                                                                   
        """,1 + Fore.LIGHTYELLOW_EX))
            enter()
            print(str(text) + Fore.RESET) 
        elif int(option) == 5:
            print(Colorate.Horizontal(Colors.yellow,r"""
      _____ ___ ___ 
     |_   _|_ _| _ \
       | |  | ||  _/
       |_| |___|_|                                                                    
        """, 1))
            enter()
            print(Fore.LIGHTYELLOW_EX + str(text) + Fore.RESET) 
    if int(option) not in (1,2,3,4,5):
        raise ValueError("The option from tip function is not an integer (1,2,3,4,5) ! [ENDA CAPP]")

#Define a banner generator
def banner(text:str,font:str="standard"):
    asciiArt(text,font)