import pyautogui as MI
import groups as group
import time
import math
import finishBattle as CB
MI.Pause = 0.001

warTime = True
killLimit = -1
maxBattles = -1

Human = False
NPCone = True
PMFlag = False
WCFlag = False

turns = 0




###Function to sleep when I click settings
def settings():
    settings = MI.locateCenterOnScreen ("images/settings.png", confidence = 0.90, region = (975,393,200,140))
    while(settings):
        print("\t\tSettings")
        time.sleep(1)
        settings = MI.locateCenterOnScreen ("images/settings.png", confidence = 0.90)




##Function to move mouse after we click everything
def mouseMove():
    MI.moveTo(1425, 365)




##Function to check for PMS
def privateChat():
    global PMFlag
    PM = MI.locateCenterOnScreen('images/skills/pm.png', confidence = 0.70, region = (1770, 210, 100, 50))
    if(PM and not PMFlag):
        print("We have received a PM")
        PMFlag = True
        playerSS = "images/PMs/" + "PM_" + str(time.time()) + ".png"
        MI.screenshot(playerSS, region = (960,215,960,640))




#Function to check for WC on 1
def warCommander():
    global WCFlag
    global turns
    if(not WCFlag and turns == 0):
        WC = MI.locateCenterOnScreen('images/skills/one.png', confidence = 0.70, region = (1067, 635, 15, 25))
        if(WC): 
            print("\t\tWC empty on next win\n")
            WCFlag = True




###Function for healing
def checkForHeal():
    notHeal = MI.locateCenterOnScreen('images/skills/health.png', confidence = 0.90, region = (960, 805, 100, 40))
    if not notHeal:
        print("\t\tHealing\n")

        ##HP Booster
        MI.click(1819,622)

        ##Medic
        MI.click(MI.locateCenterOnScreen('images/skills/medicSkill.png', confidence = 0.70, region = (1020,665,680,90)))

        mouseMove()
    privateChat()




###Function for healing with people
def checkForHealHuman():
    notHeal = MI.locateCenterOnScreen('images/skills/health.png', confidence = 0.90, region = (960, 805, 100, 40))
    if not notHeal:
        print("\t\tHealing against humans\n")

        ##Medic
        MI.click(MI.locateCenterOnScreen('images/skills/medicSkill.png', confidence = 0.70, region = (1020,665,680,90)))
        
        ##HP Booster
        MI.click(1819,622)

        mouseMove()
    privateChat()




##Means we have a real player in our battle and we will spam it with attacks
def RealPlayer():
    global warTime
    global NPCone
    global WCFlag
    global turns
    
    while(MI.locateCenterOnScreen('images/skills/fame.png', confidence = 0.70, region = (1085, 230, 100, 170))):
        privateChat()
        humanBottom = MI.locateCenterOnScreen('images/skills/fame.png', confidence = 0.70, region = (1085, 330, 100, 70))
        if(humanBottom): 
            bottom = True
            coords = (1126, 773)
        else:
            bottom = False
            coords = (1161, 551)

        print(coords, "bottom?:",bottom)
        
        Human = MI.locateCenterOnScreen('images/skills/fame.png', confidence = 0.70, region = (1085, 230, 100, 170))
        while(Human):
            privateChat()
            if(MI.locateCenterOnScreen('images/skills/strike.png', confidence = 0.90, region = (1391,535,33,46)) or MI.locateCenterOnScreen("images/skills/cancelMove.png", confidence = 0.85, region = (1374,522,135,48))):
                if(warTime):
                    if(not WCFlag and turns == 0):
                        ##Checks for WC on 1
                        warCommander()

                ##Heal command
                checkForHealHuman()
                if not(MI.locateCenterOnScreen("images/skills/smokeNPC.png", confidence = 0.70, region = (970,265,200,200))):
                    ##Should be doing smoke
                    group.attackHuman(coords, False)
                    mouseMove()
                else:
                    group.attackHuman(coords, NPCone)
                    mouseMove()
                turns = turns + 1
                settings()
            if bottom:
                Human = MI.locateCenterOnScreen('images/skills/fame.png', confidence = 0.70, region = (1085, 330, 100, 70))
            else:
                Human = MI.locateCenterOnScreen('images/skills/fame.png', confidence = 0.70, region = (1085, 230, 100, 70))
        
        NPCone = False
        print("\t\tDeadHuman\n")
        



##Will go into the different groups of NPCs to decide certain attacks per certain NPC
##Decides if NPC is top or bottom and will send info to selectMoveOn
def attackWho(NPC, coords):
    global Human
    if not (MI.locateCenterOnScreen('images/skills/NPCLevelBubble.png', confidence = 0.70, region = (1088, 233, 45, 153) or Human)):
        return False

    if NPC == "admin":
        bottomNPC = True
    
    elif NPC == "corporate" and coords.y > 465:
        bottomNPC = True

    elif NPC == "dragonoid" and coords.y > 430:
        bottomNPC = True

    elif NPC == "ebil" and coords.y > 430:
        bottomNPC = True

    elif NPC == "electro" and coords.y > 400:
        bottomNPC = True

    elif NPC == "exile" and coords.y > 600:
        bottomNPC = True

    elif NPC == "frost" and coords.y > 400:
        bottomNPC = True

    elif NPC == "gamma" and coords.y > 430:
        bottomNPC = True
   
    elif NPC == "lawman" and coords.y > 470:
        bottomNPC = True

    elif NPC == "lionhart" and coords.y > 470:
        bottomNPC = True

    elif NPC == "overlord" and coords.y > 430:
        bottomNPC = True

    elif NPC == "pirate" and coords.y > 460:
        bottomNPC = True

    elif NPC == "snork" and coords.y > 430:
        bottomNPC = True

    elif NPC == "void" and coords.y > 440:
        bottomNPC = True

    elif NPC == "valery" and coords.y > 460:
        bottomNPC = True

    elif NPC == "valestra" and coords.y > 490:
        bottomNPC = True

    elif NPC == "yeti" and coords.y > 450:
        bottomNPC = True

    else:
        bottomNPC = False


    ##Mechachillids are different levels

    if(NPC == "mecha"):
        if(coords.y < 500):
            NPC = "mecha29"
        else:
            NPC = "mecha34"
            bottomNPC = True

    ##print("\t\t",NPC, "is bottom NPC?",bottomNPC, "\t\tcoords:",coords)
    selectMoveOn(NPC, coords, bottomNPC)
    return True



##Sets the group pf NPCs so we know what to do based on the input NPC
def selectMoveOn(NPC, coords, bottomNPC):
    global NPCone
    privateChat()
    ##Attacks the NPC based on the coords and name

    if bottomNPC:
        NPCPlacement(NPC, coords, 0, 0, 0, 0, 0)
       
    else:
        NPCPlacement(NPC, coords, -106, 90, -180, 96, -107)
     
    if(MI.locateCenterOnScreen('images/skills/playerbubble.png', confidence = 0.70, region = (1864, 227, 50, 50))):
        if(MI.locateCenterOnScreen('images/skills/strike.png', confidence = 0.90, region = (1391,535,33,46)) or MI.locateCenterOnScreen("images/skills/cancelMove.png", confidence = 0.85, region = (1374,522,135,48))):
            group.attack(coords, NPCone)
            mouseMove()




def NPCPlacement(NPC, coords, NPCAliveY, coordsX, coordsY, posX, posY):
    global warTime
    global NPCone
    global WCFlag
    global turns
    Smoke = False
    Attacked = False

    NPCalive = MI.locateCenterOnScreen('images/skills/NPCLevelBubble.png', confidence = 0.70, region = (1088, 339 + NPCAliveY, 45, 47))
    while(NPCalive):
        Attacked = True
        privateChat()
        if(MI.locateCenterOnScreen("images/skills/smokeNPC.png", confidence = 0.70, region = (970,265,200,200))):
            Smoke = True
        if(MI.locateCenterOnScreen('images/skills/strike.png', confidence = 0.90, region = (1391,535,33,46)) or MI.locateCenterOnScreen("images/skills/cancelMove.png", confidence = 0.85, region = (1374,522,135,48))):
            if(warTime):
                if(not WCFlag and turns == 0):
                    ##Checks for WC on 1
                    warCommander()
            
            ##Heal command
            checkForHeal()
            coords = MI.locateCenterOnScreen("images/"+ NPC + ".png", confidence = 0.80, region = (1060 + coordsX,391 + coordsY, 155, 500))
            if (not coords):
                coords = MI.locateCenterOnScreen("images/" + NPC + "_knees.png", confidence = 0.80, region = (1075,211,250,500))
            if (not coords):
                coords = (1126 + posX ,773 + posY)
    
            if (not MI.locateCenterOnScreen("images/skills/smokeNPC.png", confidence = 0.70, region = (970,265,200,200)) and Smoke):
                group.attack(coords, NPCone)
                mouseMove()
            else:
                groupSelection(NPC, coords, NPCone)
            turns = turns + 1

        settings()
        NPCalive = MI.locateCenterOnScreen('images/skills/NPCLevelBubble.png', confidence = 0.70, region = (1088, 339 + NPCAliveY, 45, 47)) 
    NPCone = False
    if Attacked:
        print("\t\tDead\n")




##Selects the group for the NPC and attacks it
def groupSelection(NPC, coords, NPCone):
    group1 = ["electro","frost"]
    group2 = ["yeti","snork","mecha34"]
    group3 = ["valestra","gamma","admin","lawman","exile"]
    group4 = ["overlord","valery","dragonoid","ebil"]
    group5 = []
    group6 = ["corporate","void"]
    group7 = ["mecha29", "pirate","lionhart"]

    if NPC in group1:
        group.groupA(NPC,coords,NPCone)
    elif NPC in group2:
        group.groupB(NPC,coords,NPCone)
    elif NPC in group3:
        group.groupC(NPC,coords,NPCone)
    elif NPC in group4:
        group.groupD(NPC,coords,NPCone)
    elif NPC in group5:
        group.groupE(NPC,coords,NPCone)
    elif NPC in group6:
        group.groupF(NPC,coords,NPCone)
    elif NPC in group7:
        group.groupG(NPC,coords,NPCone)

    ##Attack
            
    MI.click(coords)
    group.attack(coords, NPCone)
    mouseMove()




##Function for inserting war commanders into my inventory
def WCInsert():
    privateChat()

    print("\t\tAdding war commander\n")
    jugg = MI.locateCenterOnScreen('images/jugg.png', confidence = 0.7, region = (1486, 801, 100, 100))
    while(not jugg):
        jugg = MI.locateCenterOnScreen('images/jugg.png', confidence = 0.7, region = (1486, 801, 100, 100))

    ##open inventory

    inventory = MI.locateCenterOnScreen('images/skills/inventory.png', confidence = 0.85, region = (1640, 800, 40, 50))
    while(not inventory):
        inventory = MI.locateCenterOnScreen('images/skills/inventory.png', confidence = 0.85, region = (1640, 800, 40, 50))

    MI.click(inventory)
    time.sleep(0.45)

    slotempty = MI.locateCenterOnScreen('images/skills/slotempty.png', confidence = 0.85, region = (1720, 360, 70, 70))
    while(not slotempty):
        slotempty = MI.locateCenterOnScreen('images/skills/slotempty.png', confidence = 0.85, region = (1720, 360, 70, 70))
            
    ##Click Slot

    MI.click(slotempty)
    time.sleep(0.45)

    ##Click WC

    MI.click(1797,508)
    time.sleep(0.45)

    ##Insert WC

    MI.click(1614,772)
    time.sleep(0.45)              

    ##Confirm Insert

    MI.click(1565,536)
    time.sleep(0.45)

    ##Close Inventory

    MI.click(1911,248)
    print("\t\tWar commander added\n")


##################################################################################################################
##################################################################################################################


##Sets up NPCs and Battle
def Juggernaut():
    PlayerFlag = False
    battleOver = False
    numPlayers = 0

    global Human
    global warTime
    global NPCone
    global PMFlag
    global WCFlag
    global killLimit
    global maxBattles
    global turns
    ##The list of NPCs that we can be fighting

    NPCs = ["lionhart","pirate",
    "corporate","void",
    "yeti","snork","mecha","valestra","gamma","lawman","admin",
    "overlord","valery",
    "dragonoid","ebil",
    "electro","frost",
    "exile"]

    numBattles = 0
    kills = 0
    losses = 0

    ##For timing purposes

    startingTime = overallTime = time.time()

    ##Loop for doing jugg battles
    
    while(True):

        ##Checks to see if we have a PM

        privateChat()

        ##Checks to see if we are out of battle and the jugg button is available

        jugg = MI.locateCenterOnScreen('images/jugg.png', confidence = 0.7, region = (1486, 801, 100, 100))
        if(jugg):

            ##Searches for a war objective before we enter a battle and drops bomb if there is one
            if(warTime):
                objective = MI.locateCenterOnScreen('images/skills/warobjective.png', confidence = 0.70)
                if(objective):
                    MI.click(objective)
                    time.sleep(0.45)
                    MI.click(1227,535)

            ##Enters the jugg battle
            numBattles = numBattles + 1
            MI.click(jugg)

            time.sleep(1)

            ##In case of lag, keeps pressing the jugg battle as long as we see it (until we enter)

            jugg = MI.locateCenterOnScreen('images/jugg.png', confidence = 0.7, region = (1486, 801, 100, 100))
            jugg_stuck = MI.locateCenterOnScreen('images/jugg_stuck.png', confidence = 0.7, region = (1486, 801, 100, 100))
            while(jugg or jugg_stuck):
                MI.click(jugg)
                MI.click(jugg_stuck)
                time.sleep(0.25)
                jugg = MI.locateCenterOnScreen('images/jugg.png', confidence = 0.7, region = (1486, 801, 100, 100))
                jugg_stuck = MI.locateCenterOnScreen('images/jugg_stuck.png', confidence = 0.7, region = (1486, 801, 100, 100))
                
            if(numBattles == 1):
                startingTime = overallTime = time.time()
            else:
                startingTime = time.time()

            print("Battle", numBattles)
            time.sleep(5)

        ##If we are in a juggernaut battle

        elif(MI.locateCenterOnScreen('images/skills/playerbubble.png', confidence = 0.70, region = (1864, 227, 50, 50))):
            privateChat()

            ##check for fame bubble and see if we have a real player

            if(not PlayerFlag):
                PlayerFlag = True
                MI.click(1670,835)
                MI.sleep(0.35)

                Human = MI.locateCenterOnScreen('images/skills/fame.png', confidence = 0.70, region = (1085, 231, 100, 170))
                if(Human):
                    numPlayers = numPlayers + 1
                    print("\t Real Human",numPlayers,"\n")
                    playerSS = "images/realPlayers/Player"+ str(numPlayers) + "_" + str(time.time()) + ".png"
                    MI.screenshot(playerSS, region = (960,215,960,640))
                    battleOver = True
                    RealPlayer()

            coords = (1126,773)
            NPC = "admin"

            ##Search for the NPC that we will hit in Battle
            if(MI.locateCenterOnScreen('images/skills/NPCLevelBubble.png', confidence = 0.70, region = (1088, 233, 45, 153))):
                foundNPC = False
                for i in range(0,2):
                    for i in NPCs:
                        filename = "images/"+ i + ".png"
                        coords = MI.locateCenterOnScreen(filename, confidence = 0.80, region = (1075,211,250,500))
                        if(coords):
                            if(i == "exile" and coords.y < 545):
                                NPC = "admin"
                                coords = (1126,773)
                            else:
                                NPC = i
                                print("\t",NPC,"\n")
                                foundNPC = True
                                break
                        else:

                            ##If we don't find a NPC we attack the bottom NPC prioritizing strongest
                            ##attacks following a smoke screen

                            coords = (1126,773)
                            NPC = "admin"
                    if foundNPC:
                        break
                           
            privateChat()

            ##This statment continues to be run as long as we are alive or the battle is still going on

            while(MI.locateCenterOnScreen('images/skills/playerbubble.png', confidence = 0.70, region = (1864, 227, 50, 50))):
                battleOver = True
                if not (attackWho(NPC, coords)):
                    if(MI.locateCenterOnScreen('images/skills/strike.png', confidence = 0.90, region = (1391,535,33,46)) or MI.locateCenterOnScreen("images/skills/cancelMove.png", confidence = 0.85, region = (1374,522,135,48))):
                        group.attack(coords, NPCone)
                else:
                    break
                
  
        else:
            if(warTime):
                drop = MI.locateCenterOnScreen('images/skills/continue.png', confidence = 0.90, region = (1340,635,200,65))
                if(drop):
                        MI.click(drop)

            if(battleOver):
                privateChat()
                if(MI.locateCenterOnScreen('images/didYouKnow.png',confidence = 0.7, region = (1019, 752, 53, 49))):
                    kills, losses = CB.finish(kills, losses)
                    if kills < 0 and losses < 0:
                        print("X undetected")
                        return
                    group.battleDone()
                    
                    if numBattles == 0:
                        kills = losses = 0 
                    Human = False
                    battleOver = False
                    NPCone = True
                    newTime = time.time()
                    if numBattles > 0:
                        battleStats(numBattles, kills, losses, newTime, startingTime, overallTime)
                    turns = 0
                    if WCFlag:
                        WCInsert()
                        WCFlag = False
                    if PlayerFlag:
                        PlayerFlag = False
                    if PMFlag:
                        print("Done because PM")
                        return
                    if numBattles == maxBattles:
                        print("Reached quota of", maxBattles, "battle(s)")
                        return
                    if kills == killLimit:
                        print("Reached quota of", killLimit, "win(s)")
                        return

            settings()




def battleStats(numBattles, kills, losses, newTime, startingTime, overallTime):
    global turns
    print("\n\t\tBattle Stats\n") 
    print("\t\t\tBattle time:",newTime - startingTime,"second(s)\n")
    print("\t\t\tTurns:",turns,"\n")     
    print("\t\t\tWins:",kills,"\n")          
    print("\t\t\tLosses:",losses,"\n")
    if kills or losses > 1:
        print("\t\t\tWin Percent:", (kills/(losses+kills))*100,"\n")
    print("\t\t\tPer hour wins with this time:", 3600/(newTime - startingTime), "win(s)\n")
    if(numBattles>1):
        print("\t\t\tAverage battle time:", (newTime - overallTime)/numBattles, "second(s)\n")
        if kills > 1:
            print("\t\t\tWins per hour:", 3600/((newTime - overallTime)/kills), "\n")
        print("\t\t\tTime spent battling:", math.floor((newTime - overallTime)/3600), "hour(s) and", ((newTime - overallTime)%3600)/60, "minute(s) \n\n")
    else:
        print("\t\t\tTime spent battling:", newTime - overallTime, "second(s)\n\n")




Juggernaut()