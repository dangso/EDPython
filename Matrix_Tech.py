import pyautogui as MI
import playsound as PS
import time
import math
import finishBattle as CB
MI.Pause = 0.001

killLimit = -1
PMFlag = False




def privateChat():
    global PMFlag
    PM = MI.locateCenterOnScreen('images/skills/pm.png', confidence = 0.70, region = (1770, 210, 100, 50))
    ##if(PM):
        ##PS.playsound('PMSound.mp3')
    if(PM and not PMFlag):
        print("We have received a PM")
        PMFlag = True
        playerSS = "images/PMs/" + "PM_" + str(time.time()) + ".png"
        MI.screenshot(playerSS, region = (960,215,960,640))




def Matrix():
    global PMFlag
    global killLimit
    overallTime = startingTime = newTime = time.time()
    kills = losses = shards = numBattles = turns = parasite = medicSkill = maelstrom = cannon = terrify = 0
    omegaShard = battleOver = one = two = three = four = five = power =  False
    shuffle = True

    while(True):
        if(MI.locateCenterOnScreen('images/skills/playerbubble.png', confidence = 0.70, region = (1098, 254, 27, 20))):
            while(MI.locateCenterOnScreen('images/skills/playerbubble.png', confidence = 0.70, region = (1098, 254, 27, 20))):
                privateChat()
                if(MI.locateCenterOnScreen('images/skills/strike.png', confidence = 0.70,region = (1391,535,33,46))):
                    battleOver = True
                    turns = turns + 1
                    checkForHeal()

                    if(turns > 4 and shuffle):
                        parasite = MI.locateCenterOnScreen('images/skills/parasiteSkill.png', confidence = 0.5, region = (1020,665,680,90))
                        medicSkill = MI.locateCenterOnScreen('images/skills/medicSkill.png', confidence = 0.5, region = (1020,665,680,90))
                        while not parasite:
                            parasite = MI.locateCenterOnScreen('images/skills/parasiteSkill.png', confidence = 0.5, region = (1020,665,680,90))
                        regionX = parasite.x - 35
                        regionY = parasite.y - 35
                        shuffle = False

                    if(turns > 4):
                        if(MI.locateCenterOnScreen('images/skills/parasite.png', confidence = 0.70, region = (regionX,regionY,69,69))):
                            ##Maelstrom
                            MI.click(MI.locateCenterOnScreen('images/skills/maelstrom.png', confidence = 0.50,region = (1020,665,680,90)))
                    else:
                        if(MI.locateCenterOnScreen('images/skills/parasite.png', confidence = 0.85, region = (1020,665,680,90))):
                            ##Maelstrom
                            MI.click(MI.locateCenterOnScreen('images/skills/maelstrom.png', confidence = 0.50,region = (1020,665,680,90)))

                    if not (MI.locateCenterOnScreen('images/skills/matrix_low.png', confidence = 0.95, region = (1720, 240, 60, 70))):
                        killQuick(parasite, medicSkill, maelstrom, MI.locateCenterOnScreen('images/skills/plasmaCannon.png', confidence = 0.45,region = (1020,665,680,90)), terrify)

                    ##Cannon
                    ##MI.click(1050,700)
                    MI.click(MI.locateCenterOnScreen('images/skills/plasmaCannon.png', confidence = 0.45,region = (1020,665,680,90)))

                    ##Rex
                    MI.click(1690,622)

                    ##Terrify
                    ##MI.click(1540,700)
                    MI.click(MI.locateCenterOnScreen('images/skills/terrify.png', confidence = 0.5,region = (1020,665,680,90)))

                    ##Parasite
                    #MI.click(1340,700)
                    MI.click(MI.locateCenterOnScreen('images/skills/parasiteSkill.png', confidence = 0.5,region = (1020,665,680,90)))

                    ##Focused Fury
                    MI.click(1130,622)

                    ##Gate
                    MI.click(1548,622)

                    ##Rift
                    MI.click(1336,622)

                    ##Aux
                    MI.click(1406,622)

                    ##Sidearm
                    MI.click(1191,622)

                    ##Strike
                    MI.click(1434,577)

                    mouseMove()

                    time.sleep(1)

        else:
            ##Checks if we got a shard from our battle

            omegaWolfShard = MI.locateCenterOnScreen('images/omegaWolfShard.png', confidence = 0.80, region = (1321, 505, 37, 26))
            if(omegaWolfShard):
                if(not omegaShard):
                    shards = shards + 1
                    omegaShard = True
                MI.click(1440,665)

            ##Checks if the battle is over and if we win
            if battleOver:
                if(MI.locateCenterOnScreen('images/didYouKnow.png',confidence = 0.7, region = (1019, 752, 53, 49))):
                    kills, losses = CB.finish(kills, losses)
                    if kills < 0 and losses < 0:
                        print("X invisible somehow reeeeee")
                        return
                    if numBattles == 0:
                        kills = losses = 0
                    newTime = time.time()
                    if numBattles > 0:
                        battleStats(kills, losses, turns, shards, newTime, startingTime, overallTime)
                    omegaShard = battleOver = one = two = three = four = five = power = False
                    shuffle = True
                    turns = 0
                    if PMFlag:
                        print("Done because PM")
                        return
                    if(kills == killLimit):
                        print("Reached quota of", killLimit, "kill(s)")
                        return

            ##Checks for the idle screen where we see matrix

            matrix = MI.locateCenterOnScreen('images/matrix.png', confidence = 0.85, region = (1454,428,50,25))
            if(matrix):
                MI.click(1708,413)

            ##Checks for the challenge button to matrix
            
            challenge = MI.locateCenterOnScreen('images/challengeMatrix.png', confidence = 0.95, region = (996,348,173,36))
            if(challenge):
                MI.click(1063,363)
                numBattles = numBattles + 1
                print("Battle", numBattles)
                if(numBattles == 1):
                    startingTime = overallTime = time.time()
                else:
                    startingTime = time.time()
                time.sleep(1)
               



###Function for healing
def checkForHeal():
    notHeal = MI.locateCenterOnScreen('images/skills/health_matrix.png', confidence = 0.90, region = (960, 805, 100, 25))
    if not notHeal:
        ##Medic
        ##MI.click(1200,700)
        MI.click(MI.locateCenterOnScreen('images/skills/medicSkill.png', confidence = 0.70, region = (1020,665,680,90)))

        ##HP Booster
        MI.click(1819,622)

        ##Because the script likes to be funny sometimes and skip stuff once we return
        if(MI.locateCenterOnScreen('images/skills/parasite.png', confidence = 0.85, region = (1020,665,680,90))):
            ##Maelstrom
            MI.click(MI.locateCenterOnScreen('images/skills/maelstrom.png', confidence = 0.50,region = (1020,665,680,90)))

        ##Cannon
        ##MI.click(1050,700)
        MI.click(MI.locateCenterOnScreen('images/skills/plasmaCannon.png', confidence = 0.45,region = (1020,665,680,90)))

        ##Rex
        MI.click(1690,622)

        ##Terrify
        ##MI.click(1540,700)
        MI.click(MI.locateCenterOnScreen('images/skills/terrify.png', confidence = 0.5,region = (1020,665,680,90)))

        ##Parasite
        #MI.click(1340,700)
        MI.click(MI.locateCenterOnScreen('images/skills/parasiteSkill.png', confidence = 0.5,region = (1020,665,680,90)))

        ##Focused Fury
        MI.click(1130,622)

        ##Gate
        MI.click(1548,622)

        ##Rift
        MI.click(1336,622)
        

        


def killQuick(parasite, medicSkill, maelstrom, cannon, terrify):
    if not (MI.locateCenterOnScreen('images/skills/matrix_lower.png', confidence = 0.95, region = (1720, 240, 60, 70))):
        killQuicker(parasite, medicSkill, maelstrom, cannon, terrify)

    ##Cannon
    MI.click(cannon)
    ##MI.locateCenterOnScreen('images/skills/plasmaCannon.png', confidence = 0.45, region = (1020,665,680,90))

    ##Rex
    MI.click(1690,622)

    ##Parasite
    ##MI.click(parasite)
    MI.click(MI.locateCenterOnScreen('images/skills/parasiteSkill.png', confidence = 0.5, region = (1020,665,680,90)))

    ##Focused Fury
    MI.click(1130,622)

    ##Gate
    MI.click(1548,622)

    ##Rift
    MI.click(1336,622)

    
    

def killQuicker(parasite, medicSkill, maelstrom, cannon, terrify):
    ##Rex
    MI.click(1690,622)
    
    ##Cannon
    MI.click(cannon)
    ##MI.click(MI.locateCenterOnScreen('images/skills/plasmaCannon.png', confidence = 0.45, region = (1020,665,680,90)))

    ##Focused Fury
    MI.click(1130,622)

    ##Gate
    MI.click(1548,622)

    ##Rift
    MI.click(1336,622)
    
def mouseMove():
    MI.moveTo(1425, 365)


def battleStats(kills, losses, turns, shards, newTime, startingTime, overallTime):
    print("\n\t\tBattle Stats\n")
    print("\t\t\tKills:", kills,"\n")
    print("\t\t\tDeaths:", losses,"\n")
    if kills or losses > 0:
        print("\t\t\tWin Percent:", (kills/(kills + losses))*100,"\n")
    print("\t\t\tEffective Turns:", turns,"\n")
    print("\t\t\tShards:", shards,"\n") 
    print("\t\t\tCredits:", shards*5000,"\n")
    print("\t\t\tBattle time:",math.floor((newTime - startingTime)/60),"minute(s), and", math.floor(((newTime - startingTime)/60)%1*60),"second(s)\n")
    print("\t\t\tPer hour wins with this time:",3600/(newTime - startingTime),"win(s)\n")
    if(kills > 0):
        print("\t\t\tWins per hour:", 3600/((newTime - overallTime)/kills),"\n")
    print("\t\t\tTime spent battling:",math.floor((newTime - overallTime)/3600), "hour(s),", math.floor(((newTime - overallTime)%3600)/60), "minute(s), and", (((((newTime - overallTime)%3600)/60)%1)*60), "second(s)\n\n")




Matrix()