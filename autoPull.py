from colorama import Fore as c
import os
from time import sleep, time


def pull(base):
    try:

        if not os.path.exists(base):
            print(c.RED + "Error: " + c.LIGHTCYAN_EX + "Base directory does not exist." + c.RESET)
        
        else:
            os.system("cd " + base + " && git pull")
                
    except Exception as e:
        print(c.RED + "Error: " + c.LIGHTCYAN_EX + str(e) + c.RESET)
        print(c.RED + "Error: " + c.LIGHTCYAN_EX + "SEND THIS LOG TO UIOPLER" + c.RESET)

dir = "{Your directory path, make sure to replace \ with \\}"

while True:
    pull(dir)
    sleep(60 - time() % 60)
    print(c.LIGHTMAGENTA_EX + "Pulling..." + c.RESET)
