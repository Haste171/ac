import os
import re
import time
import pyautogui
import sys
import os.path
from os import path
import wmi
import subprocess
import datetime
import psutil
import colorama
from colorama import Style, init, Fore
import base64
import webbrowser
import urllib
from requests import get, post

# START of AC
init(convert=True)

print(Style.BRIGHT+Fore.GREEN+base64.b64decode(b'4paI4paI4pWXICAg4paI4paI4pWX4paI4paI4paI4paI4paI4paI4paI4pWX4paI4paI4paI4paI4paI4paI4pWXIOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVlyDilojilojilojilojilojilZcgICAgICDilojilojilojilojilojilZcgIOKWiOKWiOKWiOKWiOKWiOKWiOKVlwrilojilojilZEgICDilojilojilZHilojilojilZTilZDilZDilZDilZDilZ3ilojilojilZTilZDilZDilojilojilZfilojilojilZTilZDilZDilZDilZDilZ3ilojilojilZTilZDilZDilojilojilZcgICAg4paI4paI4pWU4pWQ4pWQ4paI4paI4pWX4paI4paI4pWU4pWQ4pWQ4pWQ4pWQ4pWdCuKWiOKWiOKVkSAgIOKWiOKWiOKVkeKWiOKWiOKWiOKWiOKWiOKVlyAg4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4paI4paI4paI4paI4paI4pWX4paI4paI4paI4paI4paI4paI4paI4pWRICAgIOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVkeKWiOKWiOKVkSAgICAgCuKVmuKWiOKWiOKVlyDilojilojilZTilZ3ilojilojilZTilZDilZDilZ0gIOKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl+KVmuKVkOKVkOKVkOKVkOKWiOKWiOKVkeKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVkSAgICDilojilojilZTilZDilZDilojilojilZHilojilojilZEgICAgIAog4pWa4paI4paI4paI4paI4pWU4pWdIOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKVkSAg4paI4paI4pWR4paI4paI4paI4paI4paI4paI4paI4pWR4paI4paI4pWRICDilojilojilZEgICAg4paI4paI4pWRICDilojilojilZHilZrilojilojilojilojilojilojilZcKICDilZrilZDilZDilZDilZ0gIOKVmuKVkOKVkOKVkOKVkOKVkOKVkOKVneKVmuKVkOKVnSAg4pWa4pWQ4pWd4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWd4pWa4pWQ4pWdICDilZrilZDilZ0gICAg4pWa4pWQ4pWdICDilZrilZDilZ0g4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWdCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA=').decode(), end='')
print(Fore.RED + " \nWelcome to VERSA Anti-Cheat!")
print()
print(Fore.WHITE + 'To start Versa Anti-Cheat type: ' + Fore.MAGENTA + "start" + Fore.WHITE + '\nTo close Versa Anti-Cheat type: ' + Fore.MAGENTA + "close" + Fore.MAGENTA)
begin1 = input("\n> ")
begin2 = ("TO STOP RECORDING, CLOSE THE PROGRAM") 

if path.exists(time.strftime("%Y.%m.%d")) == False:
    os.mkdir(time.strftime("%Y.%m.%d"))
else: begin2

if begin1 == "close": 
    sys.exit() 

if begin1 == "start":
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

    print(Fore.RED + "WARNING: " + Fore.WHITE + "PLEASE DO NOT SHOW ANY PASSWORDS / CONFIDENTIAL INFORMATION WHILE RECORDING")
    print(Fore.RED + "WARNING: " + Fore.WHITE + "TO STOP RECORDING, CLOSE THE PROGRAM")

    

output = os.popen('wmic process get description').read()

while True:


    time.sleep(15) 

    im1 = pyautogui.screenshot() 
    im1.save((time.strftime("%Y.%m.%d")) + "/" + time.strftime("%Y.%m.%d.%H.%M.%S.png"))

    print()

    print(Fore.MAGENTA + "LOG: " + Fore.BLUE + "[Image Saved] "+ Fore.WHITE + "" + (time.strftime("%Y.%m.%d.%H.%M.%S.png")))

    x = open((time.strftime("%Y.%m.%d")) + "/" + time.strftime("%Y.%m.%d.%H.%M.%S")+".txt", "w")
    x.writelines(output)

    print()
    print(Fore.MAGENTA + "LOG: " + Fore.BLUE + "[File Saved] "+ Fore.WHITE + "" + (time.strftime("%Y.%m.%d.%H.%M.%S")+".txt"))





close2 = input("CLOSE")

# HOW 2 for ASCSII print(base64.b64decode(b'put base64 string here').decode(), end='')

#print(Fore.RED + base64.b64decode(b'').decode() + "\nError: " + Fore.WHITE + "You're Discord account is not compatible with DISCORD PROT!", end='')