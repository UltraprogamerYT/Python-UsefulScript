print("Loading dependencies")
#We Load all the imports here
import time
import os
import webbrowser
from Dicts import *

#Createing User If its the first time being used

if not os.path.isfile("User"):
    import Boot

#Loading the users name
try:
    print("loading user")
    f = open("User", "r")
    user_name = f.read()
    f.close()

#if there is an error loading the user display a message
except:
    print("There was an error Loading the users information, the datafile may be corrupted or missing")

#Running the main Loop
print("starting session...\n")
while True:
    terminal_start = (user_name + "/UserX OS~$")
    user_input = input(terminal_start + ' ')
    if user_input == "help":
        helplist()
    elif user_input.startswith("cd"):
        path = user_input[3:]
