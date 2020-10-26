#berrybot
import mouse
import time
import os
import keyboard
from ahk import AHK
ahk = AHK()

#Define movements
def dragright():
    ahk.click(323, 752)
    time.sleep(1)
    ahk.mouse_drag(750, 754, speed=10, relative=False) #coords to drag to

def dragleft():
    ahk.click(323, 752)
    time.sleep(1)
    ahk.mouse_drag(7, 739, speed=10, relative=False) #coords to drag to

def dragup():
    ahk.click(323, 752)
    time.sleep(1)
    ahk.mouse_drag(329, 374, speed=10, relative=False) #coords to drag to

def dragdown():
    ahk.click(323, 752)
    time.sleep(1)
    ahk.mouse_drag(330, 999, speed=10, relative=False) #coords to drag to

#Testing movements
def calibration():
    dragright()
    time.sleep(1)
    dragleft()
    time.sleep(1)
    dragup()
    time.sleep(1)
    dragdown()

#Move back and forth on a berry bush and collects berries.
def berryfarmer():
    while True:
        dragup()
        time.sleep(1)
        dragdown()
        time.sleep(1)

#Stays in a bush, runs out and shoots, then goes back into the bush
def zombieslayer():
    while True:
        dragdown()
        print("Left the bush")
        time.sleep(0.35)
        print("Sleeping to shoot the zombies")
        dragup()
        print("Back in bush")
        time.sleep(2)


        
print("BerryBot v1.0 - First open source and public zombix bot")
time.sleep(5)
coord = mouse.get_position()
print("Current mouse pos is {}".format(coord))
print("Testing movement")
print("Reopen this tab after movement testing")
time.sleep(5)
calibration()
print("Testing complete")
time.sleep(5)
os.system("cls")
print("Calibration complete.")
time.sleep(5)
os.system("cls")
print("Choose the zombix script you want to use")
print("[1] - Berry Farmer. This script harvests berries")
print("[2] - Zombie Slayer. Fights zombies. Healing and crafting being added.")
choice = input()
if choice == "1":
    berryfarmer()
elif choice == "2":
    zombieslayer()
else:
    print("Invalid choice... Stopping")
    
