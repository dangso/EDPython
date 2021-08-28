import pyautogui as MI
import time
import math

MI.PAUSE = 0.001


def finish(kills, losses):
    if(MI.locateCenterOnScreen('images/victoryX.png',confidence = 0.85, region = (1172, 417, 137, 272))):
        kills = kills + 1
        print("\tBattle Result: Win\n")
        
    elif(MI.locateCenterOnScreen('images/defeatX.png',confidence = 0.85, region = (1193, 453, 120, 155))):
        losses = losses + 1
        print("\tBattle Result: Loss\n")

    for i in range(0,3):
        x = MI.locateCenterOnScreen('images/xButton/xNorm.png', confidence = 0.65, region = (1745, 240, 34, 35))
        if(x):
            MI.click(x)
            print("\tX Button Pressed: xNormalized\n")
            return kills, losses

        x = MI.locateCenterOnScreen('images/xButton/xTest0.png', confidence = 0.65, region = (960, 215, 960, 650))
        if(x):
            MI.click(x)
            print("\tX Button Pressed: 0\n")
            return kills, losses
            
        x = MI.locateCenterOnScreen('images/xButton/xTest1.png', confidence = 0.65, region = (960, 215, 960, 650))
        if(x):
            MI.click(x)
            print("\tX Button Pressed: 1\n")
            return kills, losses

        x = MI.locateCenterOnScreen('images/xButton/xTest2.png', confidence = 0.65, region = (960, 215, 960, 650))
        if(x):
            MI.click(x)
            print("\tX Button Pressed: 2\n")
            return kills, losses

        x = MI.locateCenterOnScreen('images/xButton/xTest3.png', confidence = 0.65, region = (960, 215, 960, 650))
        if(x):
            MI.click(x)
            print("\tX Button Pressed: 3\n")
            return kills, losses

        x = MI.locateCenterOnScreen('images/xButton/xTest4.png', confidence = 0.70, region = (960, 215, 960, 650))
        if(x):
            MI.click(x)
            print("\tX Button Pressed: 4\n")
            return kills, losses

        x = MI.locateCenterOnScreen('images/xButton/xTest5.png', confidence = 0.80, region = (960, 215, 960, 650))
        if(x):
            MI.click(x)
            print("\tX Button Pressed: 5\n")
            return kills, losses

        x = MI.locateCenterOnScreen('images/xButton/xTest6.png', confidence = 0.70, region = (960, 215, 960, 650))
        if(x):
            MI.click(x)
            print("\tX Button Pressed: 6\n")
            return kills, losses
            
        x = MI.locateCenterOnScreen('images/xButton/xTest7.png', confidence = 0.65, region = (960, 215, 960, 650))
        if(x):
            MI.click(x)
            print("\tX Button Pressed: 7\n")
            return kills, losses

        x = MI.locateCenterOnScreen('images/xButton/xTest8.png', confidence = 0.65, region = (960, 215, 960, 650))
        if(x):
            MI.click(x)
            print("\tX Button Pressed: 8n")
            return kills, losses
        
        x = MI.locateCenterOnScreen('images/xButton/xTest9.png', confidence = 0.65, region = (960, 215, 960, 650))
        if(x):
            MI.click(x)
            print("\tX Button Pressed: 9\n")
            return kills, losses

        x = MI.locateCenterOnScreen('images/xButton/xTest10.png', confidence = 0.65, region = (960, 215, 960, 650))
        if(x):
            MI.click(x)
            print("\tX Button Pressed: 10\n")
            return kills,losses

        x = MI.locateCenterOnScreen('images/xButton/xTest11.png', confidence = 0.65, region = (960, 215, 960, 650))
        if(x):
            MI.click(x)
            print("\tX Button Pressed: 11\n")
            return kills, losses

        x = MI.locateCenterOnScreen('images/xButton/xTest12.png', confidence = 0.65, region = (960, 215, 960, 650))
        if(x):
            MI.click(x)
            print("\tX Button Pressed: 12\n")
            return kills, losses

        x = MI.locateCenterOnScreen('images/xButton/xTest13.png', confidence = 0.65, region = (960, 215, 960, 650))
        if(x):
            MI.click(x)
            print("\tX Button Pressed: 13\n")
            return kills, losses

        x = MI.locateCenterOnScreen('images/xButton/xTest14.png', confidence = 0.65, region = (960, 215, 960, 650))
        if(x):
            MI.click(x)
            print("\tX Button Pressed: 14\n")
            return kills, losses

        x = MI.locateCenterOnScreen('images/xButton/xTest15.png', confidence = 0.65, region = (960, 215, 960, 650))
        if(x):
            MI.click(x)
            print("\tX Button Pressed: 15\n")
            return kills, losses    

    playerSS = "images/xDetectErrors/DetectError" + "_" + str(time.time()) + ".png"
    MI.screenshot(playerSS, region = (960,215,960,640))
    print("\tX Button undetected\n")
    return -99999,-99999