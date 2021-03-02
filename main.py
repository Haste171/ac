import os
import time
import pyautogui
import sys
import os.path
from os import path
import wmi
import subprocess
import datetime
import psutil

print(" Welcome to VERSA Anti Cheat")
print()
begin1 = input(" Are you ready to start recording? (y/n): ")

begin2 = (" TO STOP RECORDING, CLOSE THE PROGRAM") 

if path.exists(time.strftime("%Y.%m.%d")) == False:
    os.mkdir(time.strftime("%Y.%m.%d"))
else: begin2

if begin1 == "no": 
    sys.exit() 

if begin1 == "n": 
    sys.exit()

if begin1 == "yes":
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

    print(" WARNING: PLEASE DO NOT SHOW ANY PASSWORDS / CONFIDENTIAL INFORMATION WHILE RECORDING")
    print()
    print(" TO STOP RECORDING, CLOSE THE PROGRAM")

if begin1 == "y":
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print(" WARNING: PLEASE DO NOT SHOW ANY PASSWORDS / CONFIDENTIAL INFORMATION WHILE RECORDING")
    print()
    print(" TO STOP RECORDING, CLOSE THE PROGRAM")

output = os.popen('wmic process get description').read()

while True:


    time.sleep(15) 

    im1 = pyautogui.screenshot() 
    im1.save((time.strftime("%Y.%m.%d")) + "/" + time.strftime("%Y.%m.%d.%H.%M.%S.png"))

    print()

    print(" Image Saved: " + "" + (time.strftime("%Y.%m.%d.%H.%M.%S.png")))

    x = open((time.strftime("%Y.%m.%d")) + "/" + time.strftime("%Y.%m.%d.%H.%M.%S")+".txt", "w")
    x.writelines(output)

    print()
    print(" File Saved: " + "" + (time.strftime("%Y.%m.%d.%H.%M.%S")+".txt"))



 


        
close2 = input("CLOSE")