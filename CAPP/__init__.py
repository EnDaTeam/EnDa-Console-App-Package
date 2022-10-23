#The EnDa Console Application Package's Main Script

#Import needed modules
from Dependencies import *
from Commands import *

#Define an enter function (space)
def enter(lines=1):
    for i in range(lines):
        print()
    
#Define a clear console function
def clearConsole():
    varietycommandexecutor("clear","cls")

#Define a custom command executor
def customCommandExecutor(command1,variety=0,command2=0):
    try:
        if variety:
            varietycommandexecutor(command1,command2)
        else:
            commandexecutor(command1)
    except:
        raise ValueError("Something went wrong in Custom Command Executor![ENDA CAPP]")

#Define an error output function
def error(string,exiting=0,option=1): 
    #String = what do you want to print
    #Exiting = do you want to exit after erroring
    #Option = there are more option of printing the error
    try:
        int(option)
    except:
        raise ValueError("Please enter an avaible option to error function![ENDA CAPP]")
    else:
        if int(option) == 1:
            print(Fore.RED + "[ERROR]" + Fore.WHITE + " >> " + Fore.LIGHTRED_EX + str(string) + Fore.RESET)
        elif int(option) == 2:
            print(Fore.RED + r"""
 _________________ ___________ 
|  ___| ___ \ ___ \  _  | ___ \
| |__ | |_/ / |_/ / | | | |_/ /
|  __||    /|    /| | | |    / 
| |___| |\ \| |\ \\ \_/ / |\ \ 
\____/\_| \_\_| \_|\___/\_| \_|

            """)
            print(Fore.LIGHTRED_EX + "\t" + str(string) + Fore.RESET)
        elif int(option) == 3:
            print(Fore.RED + """           
▒█▀▀▀ ▒█▀▀█ ▒█▀▀█ ▒█▀▀▀█ ▒█▀▀█ 
▒█▀▀▀ ▒█▄▄▀ ▒█▄▄▀ ▒█░░▒█ ▒█▄▄▀ 
▒█▄▄▄ ▒█░▒█ ▒█░▒█ ▒█▄▄▄█ ▒█░▒█
                    """)
            print(Fore.LIGHTRED_EX + "\t" + str(string) + Fore.RESET)
        elif int(option) == 4:
            print(Fore.RED + "ERROR" + Fore.WHITE + " : " + Fore.LIGHTRED_EX + str(string) + Fore.RESET)
        else:
            raise ValueError("Please enter an avaible option to error function![ENDA CAPP]")
        if exiting:
            print(Fore.RESET)
            exit()

#Define a random value generator for banners
def bannerValue(start,end):
    try:
        int(start)
        int(end)
    except:
        raise ValueError("Please enter integers on random value generator for banner!")
    else:
        value = random.randint(start,end)
    return value