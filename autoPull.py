from colorama import Fore as c
import os, threading
from time import sleep

seconds = 3600 #change to what you want

def pull(base):
    
    try:
        #Checks if the directory exists on your machine
        if not os.path.exists(base):
            print(c.RED + "Error: " + c.LIGHTCYAN_EX + "Base directory does not exist." + c.RESET)
        
        else:
            #if it does, it will go to the directory and pull it with git
            os.system("cd " + base + " && git pull")
                
    except Exception as e:
        #if there is an error, it will display it
        print(c.RED + "Error: " + c.LIGHTCYAN_EX + str(e) + c.RESET)
        print(c.RED + "Error: " + c.LIGHTCYAN_EX + "SEND THIS TO uiopler#6948 ON DISCORD" + c.RESET)

while True:

    sleep(seconds)
    #Replace "Your Directory" with the specified one, please make sure to replace "/" with "//", example C:/Users/... --> C://Users//...
    #You can add more directories if you want, just add a comma and add it (Make sure to put the dir in Elipsis / Quotation mark (these are called Elipsis / Quotation mark -> "" ))
    DIRECTORIES = ["Your Directory"]
    #loops through the directories 

    for i in DIRECTORIES:
        pull(i)
    
