import pyautogui as MI
MI.PAUSE = 0.001

group1Strike = True
group5Strike = True
groupBCore = True
groupCCore = True
groupDCore = True

def groupA(name, coords, NPCone):
    global static
    global group1Strike
    
    #Smoke, Static, Rex, Focused Fury
    if not(MI.locateCenterOnScreen("images/skills/smokeNPC.png", confidence = 0.70, region = (970,265,200,200))):
        ##Smoke
        ##MI.click(1200,707)
        MI.click(MI.locateCenterOnScreen('images/skills/smoke.png', confidence = 0.8, region = (1020,665,680,90)))

        ##Attack
        MI.click(coords)
        return

    if (MI.locateCenterOnScreen("images/skills/rex.png",confidence = 0.90, region = (1645,590,80,80))):
        ##Rex
        MI.click(1690,622)

        ##Attack
        MI.click(coords)
        return

    if(name == "electro" and NPCone and group1Strike):
        ##Strike
        MI.click(1434,577)
        
        ##Attack
        MI.click(coords)

        group1Strike = False
        
    elif(name == "frost" and NPCone and group1Strike):
        ##Strike
        MI.click(1434,577)
        
        ##Attack
        MI.click(coords)

        group1Strike = False

    ##Focused Fury
    MI.click(1130,622)

    if(not NPCone):
        #Attack
        MI.click(coords)

        #Focused Fury
        MI.click(1130,622)

        ##Frozen Rift
        MI.click(1336,622)

        ##Gate
        MI.click(1548,622)

    ##Attack
    MI.click(coords)



def groupB(name, coords, NPCone):
    global groupBCore
    #Smoke, Focused, Rex

    if not(MI.locateCenterOnScreen("images/skills/smokeNPC.png", confidence = 0.70, region = (970,265,200,200))):
        ##Smoke
        ##MI.click(1200,707)
        MI.click(MI.locateCenterOnScreen('images/skills/smoke.png', confidence = 0.8, region = (1020,665,680,90)))

        ##Attack
        MI.click(coords)
        return

    if (not NPCone and groupBCore):
        #Attack
        MI.click(coords)
        
        ##Focused Fury
        MI.click(1130,622)

        ##Frozen Rift
        MI.click(1336,622)

        #Gate
        MI.click(1548,622)

        groupBCore = False

    ##Attack
    MI.click(coords)

    ##Rex
    MI.click(1690,622)

    ##Attack
    MI.click(coords)

    ##Focused Fury
    MI.click(1130,622)

    ##Attack
    MI.click(coords)

    ##Frozen Rift
    MI.click(1336,622)

    ##Attack
    MI.click(coords)

    #Gate
    MI.click(1548,622)

    ##Attack
    MI.click(coords)
    



def groupC(name, coords, NPCone):
    global groupCCore
    #Smoke, Gate, Rex

    if not(MI.locateCenterOnScreen("images/skills/smokeNPC.png", confidence = 0.70, region = (970,265,200,200))):
        ##Smoke
        ##MI.click(1200,707)
        MI.click(MI.locateCenterOnScreen('images/skills/smoke.png', confidence = 0.8, region = (1020,665,680,90)))

        ##Attack
        MI.click(coords)
        return

    if(not NPCone and groupCCore):
        ##Attack
        MI.click(coords)

        ##Frozen Rift
        MI.click(1336,622)
        
        ##Gate
        MI.click(1548,622)

        #Focused Fury
        MI.click(1130,622)

        groupCCore = False

    ##Rex
    MI.click(1690,622)

    #Attack
    MI.click(coords)

    ##Gate
    MI.click(1548,622)

    #Attack
    MI.click(coords)
    
        


def groupD(name, coords, NPCone):
    ##Smoke, Gate, Rift
    global groupDCore

    if not(MI.locateCenterOnScreen("images/skills/smokeNPC.png", confidence = 0.70, region = (970,265,200,200))):
        ##Smoke
        ##MI.click(1200,707)
        MI.click(MI.locateCenterOnScreen('images/skills/smoke.png', confidence = 0.8, region = (1020,665,680,90)))

        ##Attack
        MI.click(coords)
        return

    if(NPCone):
        #Gate
        MI.click(1548,622)

        #Attack
        MI.click(coords)

        ##Frozen Rift
        MI.click(1336,622)

        #Attack
        MI.click(coords)

        #Focused Fury
        MI.click(1130,622)

        #Attack
        MI.click(coords)

    if(not NPCone and groupDCore):
        #Gate
        MI.click(1548,622)

        ##Frozen Rift
        MI.click(1336,622)

        #Focused Fury
        MI.click(1130,622)

        groupDCore = False    

    ##Attack
    MI.click(coords)

    if(not NPCone):
        ##Rex
        MI.click(1690,622)
        



def groupE(name, coords, NPCone):
    global group5Strike
    ##Smoke, Strike, Focused

    if not(MI.locateCenterOnScreen("images/skills/smokeNPC.png", confidence = 0.70, region = (970,265,200,200))):
        ##Smoke
        ##MI.click(1200,707)
        MI.click(MI.locateCenterOnScreen('images/skills/smoke.png', confidence = 0.8, region = (1020,665,680,90)))

        ##Attack
        MI.click(coords)
        return

    if(group5Strike and NPCone):
        ##Strike
        MI.click(1434,577)
        group5Strike = False

    ##Attack    
    MI.click(coords)
    
    #Focused Fury
    MI.click(1130,622)

    ##Attack    
    MI.click(coords)




def groupF(name, coords, NPCone):
    global group5Strike
    ##Smoke, Strike, Gate

    if not(MI.locateCenterOnScreen("images/skills/smokeNPC.png", confidence = 0.70, region = (970,265,200,200))):
        ##Smoke
        ##MI.click(1200,707)
        MI.click(MI.locateCenterOnScreen('images/skills/smoke.png', confidence = 0.8, region = (1020,665,680,90)))

        ##Attack
        MI.click(coords)
        return

    if(group5Strike):
        ##Strike
        MI.click(1434,577)
        group5Strike = False

    ##Attack    
    MI.click(coords)
    
    ##Gate
    MI.click(1548,622)

    ##Attack    
    MI.click(coords)




def groupG(name, coords, NPCone):
    ##Smoke, Static, Fury
    if not(MI.locateCenterOnScreen("images/skills/smokeNPC.png", confidence = 0.70, region = (970,265,200,200))):
        ##Smoke
        ##MI.click(1200,707)
        MI.click(MI.locateCenterOnScreen('images/skills/smoke.png', confidence = 0.8, region = (1020,665,680,90)))

        ##Attack
        MI.click(coords)
        return

    ##Static
    MI.click(MI.locateCenterOnScreen("images/skills/static.png",confidence = 0.85, region = (1020,665,680,90)))
    
    #Attack
    MI.click(coords)

    #Focused Fury
    MI.click(1130,622)

    ##Attack
    MI.click(coords)




def attack(coords, NPCone):
    ##Attack
    MI.click(coords)

    if not NPCone:
        if not(MI.locateCenterOnScreen("images/skills/smokeNPC.png", confidence = 0.70, region = (970,265,200,200))):
            ##Smoke
            ##MI.click(1200,707)
            MI.click(MI.locateCenterOnScreen('images/skills/smoke.png', confidence = 0.8, region = (1020,665,680,90)))

            ##Attack
            MI.click(coords)

    ##Rex
    MI.click(1690,622)

    ##Attack
    MI.click(coords)

    ##Focused Fury
    MI.click(1130,622)

    ##Attack
    MI.click(coords)

    ##Frozen Rift
    MI.click(1336,622)

    ##Attack
    MI.click(coords)

    ##Gate
    MI.click(1548,622)

    ##Attack
    MI.click(coords)

    ##Rexnorm
    MI.click(1614,622)

    ##Attack
    MI.click(coords)

    ##Strike
    MI.click(1434,577)
    
    ##Attack
    MI.click(coords)




def attackHuman(coords, NPCone):
    if not NPCone:
        if not(MI.locateCenterOnScreen("images/skills/smokeNPC.png", confidence = 0.70, region = (970,265,200,200))):
            ##Smoke
            ##MI.click(1200,707)
            MI.click(MI.locateCenterOnScreen('images/skills/smoke.png', confidence = 0.8, region = (1020,665,680,90)))

            ##Attack
            MI.click(coords)

    ##Rex
    MI.click(1690,622)

    ##Attack
    MI.click(coords)

    ##Gate
    MI.click(1548,622)

    ##Attack
    MI.click(coords)

    ##Frozen Rift
    MI.click(1336,622)

    ##Attack
    MI.click(coords)

    ##Focused Fury
    MI.click(1130,622)

    ##Attack
    MI.click(coords)
     
    ##Aux
    MI.click(1406,622)

    ##Attack
    MI.click(coords)

    ##Sidearm
    MI.click(1191,622)

    ##Strike
    MI.click(1434,577)
    
    ##Attack
    MI.click(coords)

    
    

def battleDone():
    global group1Strike
    global group5Strike
    global groupBCore
    global groupCCore
    global groupDCore

    group1Strike = True
    group5Strike = True
    groupBCore = True
    groupCCore = True
    groupDCore = True