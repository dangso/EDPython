This code is compiled using Python3

Make sure to have pyautogui, Pillow, and opencv-python installed on your machine or this will not work. I am not going to teach you how to install python or pyautogui (however I used pip3). Google exists for a reason.

This code works on Windows OS with modifications to numbers or images (there are a lot of images) depending on if your resolution is different than mine. This code was used on a computer with resolution 1920x1080 with the screen halved, so effectively 960x1080 starting at 959x0 (Just move the launcher to the right half of your screen). New images will need to be sized to your screen accordingly, and adjustments to the search area will be necessary if you are to not use these specifications.

If something does not work, you may have to edit some sections for confidence (how much an image can match), the region (search space), or the image itself.

This webpage may be deemed useful as I used it myself to help make this project: https://pyautogui.readthedocs.io/en/latest/screenshot.html#the-locate-functions

This is used on medium settings.

Cores to be used are Focused Fury, Frozen Rift, Improbability Gate, and Mini Rex P. If you are to use Mini Rex E, in the groups.py file in group A, change rex.png to rexE.png, and then in attack and attackHuman you might want to comment out rexNorm (with # before the line)

Juggernaut script to be ran is juggernautBH.py.
The build is in images, however you may have to change the energy cost around due to ranks. Static grenade is on 2 because of reasons of using static grenade on NPCs and then using smoke twice after being stunned by the second NPC. Having it on 2 allows me to not get 250 energy to do smoke again therefore saving a turn. Having this on 2 also allows me to focus more on shields against real players if necessary. 

At the top of the file there are options to change whether it's war or not (so we search for war commanders, collect battle drops, drop bombs etc...), if you do not use a war commander with war it will still work fine, just make sure to not have war commander initially equipped or it will equip a new primary core once it runs out the first time (only the first time though). You can also set kills or battles (I usually do kills to round off my wins). If we receive a PM, we will just stop battling after the battle is over, I do not have anything special set up because I don't see a need to. If you want to do it, feel free.

If there is an X button that is not detected, it should be sent to a directory called xDetectErrors (there is a placeholder image in there). You can then add that to finishBattle.py. Feel free to create another file to test this new addition.


There is also an Arcade Bot. This is used at being at Habuki and having the page open to the main screen (so that you can see your inventory backpack). There is a place to choose the arcade and the score.

There are also a few matrix scripts that are both very high quality (although the tech one is far better by nature). (Matrix is now  a 5% drop so that is unfortunate).

There are other scripts which seem self explanatory, they are also rightsided on the screen.

To stop any script, you can either move your mouse to one of the four corners of the screen, or click on the terminal window and press 'ctrl c'.

This has been created by Ginger.
