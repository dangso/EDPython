import pyautogui as MI
import groupsFF as group
import time
import math
MI.PAUSE = 0.001



def main():
    loops = 0
    while(True):
        loops = 0
        while(loops < 70):
            print(loops)
            ##Selina
            MI.click(1832,482)
            time.sleep(0.5)

            ##Shop
            MI.click(1106,326)
            time.sleep(0.5)

            ##Select Item
            MI.click(1258,742)
            time.sleep(0.5)

            ##Purchase Item
            MI.click(1430,535)
            time.sleep(0.5)

            ##Exit
            MI.click(1907, 242)
            time.sleep(0.5)

            loops = loops + 1

        ##Exit Again
        MI.click(1907, 242)
        time.sleep(0.5)
    
        ##Open Inventory
        inventory = MI.locateCenterOnScreen('images/skills/inventory.png', confidence = 0.85, region = (1640, 800, 40, 50))
        while(not inventory):
            inventory = MI.locateCenterOnScreen('images/skills/inventory.png', confidence = 0.85, region = (1640, 800, 40, 50))

        ##Click Inventory
        MI.click(inventory)
        time.sleep(1)
        ##Close Inventory
        MI.click(1911,248)
        time.sleep(1)
            

main()