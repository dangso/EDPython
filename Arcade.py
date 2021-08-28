import pyautogui as MI
import time
MI.PAUSE = 0.025

def main():
    num_items = 0
    total_items = 0
    max_items = 400
    while(True):
    ##open inventory
        inventory = MI.locateCenterOnScreen('images/skills/inventory.png', confidence = 0.95, region = (1640, 800, 40, 50))
        while(not inventory):
            inventory = MI.locateCenterOnScreen('images/skills/inventory.png', confidence = 0.95, region = (1640, 800, 40, 50))
        MI.click(inventory)
        time.sleep(3)

        ##Close Inventory
        MI.click(1911,248)

        time.sleep(3)

        #Click Arcade Bot
        MI.click(1556,488)

        time.sleep(3)

        arcade_selection = MI.locateCenterOnScreen('images/arcade/arcade_ff.png', confidence = 0.95, region = (960, 250, 700, 260))
        while(not arcade_selection):
            arrow = MI.locateCenterOnScreen('images/arcade/arcade_right_arrow.png', confidence = 0.95, region = (1420, 760, 100, 100))
            if(arrow):
                MI.click(arrow)
            time.sleep(1.25)
            arcade_selection = MI.locateCenterOnScreen('images/arcade/arcade_ff.png', confidence = 0.999, region = (960, 250, 700, 260))

        while(arcade_selection):
            score = MI.locateCenterOnScreen('images/arcade/arcade_score_100000.png', confidence = 0.90, region = (1510, 500, 90, 35))
            if(score):
                print("Score over 65000\n\tDone")
                exit = MI.locateCenterOnScreen('images/arcade/arcade_x.png', confidence = 0.95, region = (1850, 210, 70, 70))
                if(exit):
                    MI.click(exit)
                return
            arcade = MI.locateCenterOnScreen('images/arcade/arcade_go.png', confidence = 0.95, region = (1700, 700, 200, 175))
            if(arcade):
                MI.click(arcade)
                

            item = MI.locateCenterOnScreen('images/skills/continue.png', confidence = 0.95, region = (1340,635,200,65))
            while(not item):
                time.sleep(0.5)
                item = MI.locateCenterOnScreen('images/skills/continue.png', confidence = 0.95, region = (1340,635,200,65))
            if(item):
                MI.click(item)
                num_items = num_items + 1
                total_items = total_items + 1
                if(num_items >= max_items):
                    print("400 tokens spent, resetting AFK timer")
                    time.sleep(1)
                    num_items = 0
                    exit = MI.locateCenterOnScreen('images/arcade/arcade_x.png', confidence = 0.95, region = (1850, 210, 70, 70))
                    if(exit):
                        MI.click(exit)
                        arcade_selection = False
                        time.sleep(1)
                time.sleep(0.25)

main()