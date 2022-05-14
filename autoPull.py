from colorama import Fore as c
import os, threading
from time import sleep, time

seconds =(3) #change to what you want

def pull(base):
    
    try:

        if not os.path.exists(base):
            print(c.RED + "Error: " + c.LIGHTCYAN_EX + "Base directory does not exist." + c.RESET)
        
        else:
            os.system("cd " + base + " && git pull")
                
    except Exception as e:
        print(c.RED + "Error: " + c.LIGHTCYAN_EX + str(e) + c.RESET)
        print(c.RED + "Error: " + c.LIGHTCYAN_EX + "SEND THIS LOG TO UIOPLER" + c.RESET)

while True:
    sleep(seconds)

    DIRECTORIES = ["C:\\Users\\Administrator\\Documents\\GitHub\\OPW", "C:\\Users\\Administrator\\Documents\\GitHub\\OPW\\FXServer\\resources\\[cars]\\OPWVeh", "C:\\Users\\Administrator\\Documents\\GitHub\\OPW\\FXServer\\resources\\[scripts]\\opwassets\\opwtrial\\OPWTrial"]
    for i in DIRECTORIES:
        pull(i)