__author__ = 'Noah Vendrig'
__license__ = 'MIT'  # copy of the license available @ https://prodicus.mit-license.org/
__version__ = '2.9'
__email__ = 'noah.vendrig@education.nsw.gov.au'
__github__ = "github.com/noahvendrig"  # @noahvendrig
__course__ = 'Software Design and Development'
__date__ = '30/07/2021'
__description__ = '\'Samson\' is a Modern Recreation of text-based adventure game Hunt the Wumpus (1973)'
__info__ = "info available at: noahvendrig.com/#about"  # some info available here
__pyver__ = '3.8.10'
__pygamever__ = '2.0.1'
# ====================================== Imports ======================================
# pygame 2.0.1 (SDL 2.0.14, Python 3.8.10)
import pygame
# from sys import exit, float_repr_style
import sys
import os
from sys import *
import random
from pygame.locals import *
import re
import time
import ctypes
import pygame.gfxdraw
# =====================================================================================


class hazard:  # create a hazard class for all hazards (wumpus, bats cave)
    def __init__(self):  # function that activates on start
        # self.type = "hazard"
        self.pos = getRandomNode()  # set the position to a random node in the graph
        self.alertDistance = 1


class wumpus(hazard):
    def __init__(self):
        hazard.__init__(self)
        self.type = "wumpus"


class Lion(hazard):
    def __init__(self):
        hazard.__init__(self)
        self.type = "lion"


class bat(hazard):
    def __init__(self):
        hazard.__init__(self)
        self.type = "bat"


class player:
    def __init__(self):
        self.type = "player"
        self.pos = getRandomNode()

    def detectHazardCollision(self, playerPos, wumpusInstance, lions, bats):
        if playerPos in [wumpusInstance.pos]:
            return wumpusInstance

        for lion in lions:
            if playerPos == lion.pos:
                return lion

        for bat in bats:
            if playerPos == bat.pos:
                return bat

        else:
            return "null"


def blockPrint():
    sys.stdout = open(os.devnull, 'w')


def enablePrint():
    sys.stdout = sys.__stdout__


def getChildren(graph, nodesAtLevel, hazardPos, currLevel):
    visited = []  # set visited to empty again
    currLevel += 1  # increase level number.
    for node in nodesAtLevel:
        visited.extend(
            graph[node]
        )  # add the connecting nodes to the list of visited nodes.
        visited = list(
            set(visited)
        )  # convert to set to remove duplicate nodes then convert back to list to keep extending
        # print(node)

    # print("visited:", visited)
    if (
        hazardPos not in visited
    ):  # check that the hazard' pos isn't in the set of nodes that were just added to visited
        # print("\n")
        return getChildren(
            graph, visited, hazardPos, currLevel
        )  # call the function again to recursively search through each layer

    else:
        return currLevel


def showTimedText(x, y, duration, content, fontColour, font, screen, startTime):
    # text = None
    # if isinstance(content, (float, int, str, list, dict, tuple)):

    #     text = font.render(content, True, fontColour)
    # else:
    #     text= content

    try:
        text = font.render(content, True, fontColour)
    except:
        text = content

    if time.time() - startTime < duration:  # while it hasnt been duration in seconds
        screen.blit(text, (x, y))  # draw on screen
        # pygame.display.update()


def validInputReceived(graph, currNode, keyNum, wumpusInstance, lions, bats, playerInstance):

    currNode = changeNode(graph, currNode, keyNum)
    wumpusDist = min(findHazard(graph, currNode, wump.pos)
                     for wump in [wumpusInstance])  # change to wumpus list
    # wumpusDist = findHazard(graph, currNode, wumpusInstance.pos)
    lionDist = min([findHazard(graph, currNode, lion.pos) for lion in lions])
    batDist = min([findHazard(graph, currNode, bat.pos) for bat in bats])
    # print(f"{lionDist = }")
    # print(f"{batDist = }")
    return currNode, wumpusDist, lionDist, batDist


def findHazard(graph, playerPos, hazardPos):

    currLevel = 0
    distance = 0

    if playerPos != hazardPos:
        distance = getChildren(graph, [playerPos], hazardPos, currLevel)
    else:
        distance = 0

    # print(f"Hazard found {distance} nodes away from player at {playerPos}")
    return distance


def changeNode(graph, currNode, direction):  # direction: 0 = left, 1 = middle, 2=right
    nextNode = graph[currNode][direction]
    # print("moving from %s to %s" % (currNode, nextNode))
    return nextNode


def showText(currNode, w, h, fontColour, font, screen, graph, hazardDistance, charges):
    tH = h/2 - 75
    roomL_X = 400
    roomL_Y = tH
    roomM_X = 885
    roomM_Y = tH
    roomR_X = 1275
    roomR_Y = tH

    currRoom_X = roomM_X
    currRoom_Y = 800

    white = (255, 255, 255)

    # DISTANCE

    for key in hazardDistance:
        if hazardDistance[key] == 1:
            displayAdjustment = 700
            x_distTxt = h/10
            if key == "wumpusDistance":

                distanceTxt = font.render(
                    "The Philistines are nearby...",
                    True,
                    fontColour,  # finds integers in the string e.g. "19" in "n19" to display
                )
                # distanceTxt = font.render(
                #     f"{key} is %s nodes away" % hazardDistance[key],
                #     True,
                #     fontColour,  # finds integers in the string e.g. "19" in "n19" to display
                # )

                # draw on screen
                screen.blit(distanceTxt, (x_distTxt, 800))
                displayAdjustment += 125

            if key == "lionDistance":
                # print(f"{key} = {hazardDistance[key]}")
                distanceTxt = font.render(
                    "You can hear soft purrs nearby... It might be a lion",
                    True,
                    fontColour,  # finds integers in the string e.g. "19" in "n19" to display
                )

                # draw on screen
                screen.blit(distanceTxt, (x_distTxt, 850))
                displayAdjustment += 125

            if key == "batDistance":
                # print(f"{key} = {hazardDistance[key]}")
                distanceTxt = font.render(  
                    "You can hear bats nearby",
                    True,
                    fontColour,  # finds integers in the string e.g. "19" in "n19" to display
                )

                # draw on screen
                screen.blit(distanceTxt, (x_distTxt, 900))
                displayAdjustment += 125

    currRoom_Txt = font.render(  # render the text that displays the current room the player is in
        "Cave " + (re.findall("[0-9]+", currNode)[0]),
        True,
        white,  # finds integers in the string e.g. "19" in "n19" to display
    )
    screen.blit(currRoom_Txt, (currRoom_X, currRoom_Y))  # draw text on screen

    RoomL_Txt = font.render(  # render the text that displays the the player is in if they choose to move left
        "Cave " + (re.findall("[0-9]+", graph[currNode][0])[0]),
        True,
        white,  # finds integers in the string e.g. "19" in "n19" to display from the 1st node in the graph corresponding to the current room
    )
    screen.blit(RoomL_Txt, (roomL_X, roomL_Y))  # draw text on screen

    RoomM_Txt = font.render(  # render the text that displays the the player is in if they choose to move up
        "Cave " + (re.findall("[0-9]+", graph[currNode][1])[0]),
        True,
        white,  # finds integers in the string e.g. "19" in "n19" to display from the 2nd node in the graph corresponding to the current room
    )
    screen.blit(RoomM_Txt, (roomM_X, roomM_Y))  # draw on screen

    RoomR_Txt = font.render(  # render the text that displays the the player is in if they choose to move right
        "Cave " + (re.findall("[0-9]+", graph[currNode][2])[0]),
        True,
        white,  # finds integers in the string e.g. "19" in "n19" to display from the 3rd node in the graph corresponding to the current room
    )
    screen.blit(RoomR_Txt, (roomR_X, roomR_Y))  # draw on screen

    charge_Txt = font.render(
        str(charges)+" charges remaining",
        True,
        white)
    screen.blit(charge_Txt, (roomM_X, 925))


def getRandomNode():
    num = random.randint(1, 20)
    node = "n" + str(num)
    return node


# def lionDeath(fontColour, font, screen):
#     # deathTxt = font.render("YOU FELL INTO A lion",True,fontColour)
#     # screen.blit(deathTxt, (200, 350))  # draw on screen
#     showTimedText(300, 400, 5, "YOU FELL INTO A lion LO IT WORKS",
#                   fontColour, font, screen)


def showBat(screen, batImg):
    screen.blit(batImg, (400, 100))
    pygame.display.update()


class TextObj():
    def __init__(self, name, x, y, txt, w=1920, h=1080):
        self.x = x
        self.y = y
        self.txt = txt
        self.w = w
        self.h = h
        self.name = name
        # self.posRect = pygame.Rect(self.x, self.y, self.w, self.h)
    def draw(self, font, screen, fontColour=(255, 255, 255)):
        btnText = font.render(self.txt, True, fontColour)
        self.posRect = btnText.get_rect(topleft=(self.x, self.y))
        # posRect = pygame.draw.rect(screen, [0, 0, 0], [50, 50, 90, 180], 1)
        screen.blit(btnText, self.posRect)

    def Hover(self, mousePos):
        if self.posRect.collidepoint(mousePos):
            return True
        else:
            return False


def Charge(direction, playerPos, charges, wumpusPos, graph):
    print(f"{playerPos= }")
    print(f"{graph[playerPos][direction] = }")
    if charges >= 0:
        if wumpusPos == graph[playerPos][direction]:
            print("##   charge hit work")
            return True

        else:
            return False
    else:
        return False

class Leaderboard(): # Class for the leaderboard
    def __init__(self, screen, regularFont, smallFont, bg):
        self.font = regularFont
        self.smallFont = smallFont #using two different fonts so this is the smaller one
        self.scores = [] # scores starts as an empty list
        self.screen = screen
        self.maxScores = 8 # only top 8 scores displayed on the screen
        self.bg = bg
        self.reducedScores = [] # reducedScores is a list of the scores that are displayed on the screen
    def AddResult(self, result):
        self.scores.append(result)

    def Show(self):
        # bg = self.screen.fill((255,255,255))
        white = (255,255,255)
        self.screen.blit(self.bg, (1, 1))
        numTexts = []
        scoreTexts = []
        if self.scores == []:
            self.screen.blit(self.smallFont.render("Win a game to add a score to the leaderboard!", True, white), (250,250))
        else:
            self.scores.sort(reverse=True) # sort the list in descending order so the highest score is displayed first
            if len(self.scores) > self.maxScores:
                self.reducedScores = self.scores[:self.maxScores]
            for i in range(len(self.reducedScores)):#range(self.maxScores):
                numTextInstance  = TextObj("numText", 250, 100*i+250, str(i+1))
                scoreTextInstance = TextObj("scoreText", 400, 100*i+250, str(int(self.reducedScores[i])))
                numTexts.append(numTextInstance)
                scoreTexts.append(scoreTextInstance)

                num = numTexts[i]
                score = scoreTexts[i]
                num.draw(self.font, self.screen, white)
                score.draw(self.font, self.screen, white)
        
        # print(f"{len(self.scores)}, {self.scores =}")
        
        title = self.font.render("Leaderboard", True, white) #title text

        self.screen.blit(title, (250,90)) #draw title


class Controls():
    def __init__(self, screen, regularFont, smallFont, bg):
        self.screen = screen
        self.font = regularFont
        self.smallFont = smallFont
        self.bg = bg
    def Show(self):
        # bg = self.screen.fill((0,255,255))
        self.screen.blit(self.bg, (1, 1))
        h = 150
        white = (255,255,255)
        text = ["Use the arrow keys  ← ↑ → to navigate across the cave system",
         "Charge into an adjacent cave by pressing left-shift then the corresponding arrow key ← ↑ →",
        "Exit the game using esc, closing the window or \'Quit\' if in the menu.",
        "Navigate the menu using the arrow keys ↑ ↓ or the cursor to change the selection, and spacebar or clicking the button to advance", "Hit Enter to go back to the main menu"]
        for str in text:
            if len(str) > 80:
                h += 100
                slice1 = str[0:74]
                slice2 = str[74:] # not expecting more than 150 characters in a string
                textObj1 = TextObj("text", 50, h, slice1)
                h+=60
                textObj2 = TextObj("text", 50, h, slice2)
                textObj1.draw(self.smallFont, self.screen, (white))
                textObj2.draw(self.smallFont, self.screen, (white))
            else:
                h += 100
                textObj = TextObj("text", 50, h, str)
                textObj.draw(self.smallFont, self.screen, (255,255,255))
            title = self.font.render("Control", True, white) #title text

            self.screen.blit(title, (250,90)) #draw title

class Rules():
    def __init__(self, screen, regularFont, extraSmallFont, bg):
        self.screen = screen
        self.font = regularFont
        self.extraSmallFont = extraSmallFont
        self.bg = bg
    def Show(self):
        white = (255,255,255)
        # bg = self.screen.fill((0,255,255))
        self.screen.blit(self.bg, (1, 1))
        h = 80
        text = ["\'Samson\' is a game in which the player takes upon the form of an ancient hero named Samson.",
        "He is stuck in a cave, and must eliminate a massive army of Philistines before they make advancements towards the territory of his people",
        "He must navigate throughout a complex cave network of 20 caves, filled with dangerous creatures such as lions and bats whilst also attempting to find the army",
         "If Samson wonders into a cave filled with bats then he is dazed and walks far into a random cave in the network.",
         "If he stumbles upon a mighty lion, he will be unable to defend himself and will suffer mortal wounds.",
          "If Samson walks into a cave full of Philistines, then he will be killed immediately however there is a way he can defeat them.",
          "Using his keen senses and clever mind, if he charges into a cave full of Philistines then his mighty power will be unleashed, and they will all be slain",
          "This means that his people are saved and he may exit the cave."]
        for str in text:
            if len(str) > 100:
                h += 70
                slice1 = str[0:99]
                slice2 = str[99:] # not expecting more than 200 characters in a string
                textObj1 = TextObj("text", 20, h, slice1)
                h+=60
                textObj2 = TextObj("text", 20, h, slice2)
                textObj1.draw(self.extraSmallFont, self.screen,white)
                textObj2.draw(self.extraSmallFont, self.screen, white)
            else:
                h += 70
                textObj = TextObj("text", 50, h, str)
                textObj.draw(self.extraSmallFont, self.screen, white)

        title = self.font.render("How the Game Works", True, white) #title text

        self.screen.blit(title, (250,90)) #draw title
def main():

    graph = {
        "n1": ["n2", "n5", "n8"],
        "n2": ["n10", "n3", "n1"],
        "n3": ["n2", "n4", "n12"],
        "n4": ["n3", "n5", "n14"],
        "n5": ["n1", "n4", "n6"],
        "n6": ["n5", "n7", "n15"],
        "n7": ["n6", "n8", "n17"],
        "n8": ["n1", "n7", "n9"],
        "n9": ["n8", "n10", "n18"],
        "n10": ["n11", "n9", "n2"],
        "n11": ["n10", "n12", "n19"],
        "n12": ["n3", "n11", "n13"],
        "n13": ["n12", "n14", "n20"],
        "n14": ["n4", "n13", "n20"],
        "n15": ["n6", "n14", "n16"],
        "n16": ["n15", "n17", "n20"],
        "n17": ["n7", "n16", "n18"],
        "n18": ["n9", "n17", "n19"],
        "n19": ["n11", "n18", "n20"],
        "n20": ["n13", "n16", "n19"],
    }

    pygame.init()
    pygame.mixer.init()

    

    # devMode = False
    # devInput = input("enable dev mode? (Y/N) ")
    # if devInput.lower == "Y":
    #     devMode = True
    # else:
    #     devMode = False

    # if devMode:
    #     enablePrint()
    # else:
    #     blockPrint()

    # lionSound = pygame.mixer.music("./audio/lion.mp3")
    menuSound = pygame.mixer.Sound("./audio/menu.mp3")
    victorySound = pygame.mixer.Sound("./audio/victory.mp3")
    # allow for multiple channle use, so that sounds can be played over each other
    pygame.mixer.set_num_channels(5)
    # lionSound.play()
    # wumpusSound.play()

    # arialFont = pygame.font.SysFont("Arial", 30)
    frameCount = 0

    user32 = ctypes.windll.user32
    screenSize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(
        1)  # get the resolution of the user's computer
    if screenSize[0]/screenSize[1] != 16/9:  # if the resolution is not 16:9
        # TODO: make the game window size shrink so that a 16:9 ratio is maintained but fill the excess with a black background
        w = screenSize[0]  # width of the screen
        h = screenSize[1]  # height of the screen
    else:
        w = screenSize[0]  # width of the screen
        h = screenSize[1]  # height of the screen

    bgColour = (255, 255, 255)  # background colour to white
    running = True  # the game is running

    # Set the name of the window to 'Samson'
    pygame.display.set_caption("Samson")
    # Set the resolution of the screen
    screen = pygame.display.set_mode((w, h))
    fontColour = (0, 0, 0)  # default font colour I'm using is white

    # font = ("./arial.tff", 32)
    # use the free sans bold font
    font = pygame.font.Font("freesansbold.ttf", 32)

    # also use an arcade style font (medium size)
    arcadeFontMedium = pygame.font.Font("font/arcade.ttf", (int((w+h)/45))) #45
    arcadeFont60 = pygame.font.Font("font/arcade.ttf", (int((w+h)/60)))
    # also use an arcade style font (small size)
    arcadeFontSmall = pygame.font.Font("font/arcade.ttf", (int((w+h)/100)))
    arcadeFontExtraSmall = pygame.font.Font("font/arcade.ttf", (int((w+h)/120)))
    # currNode = "n1"  # set the starting node
    # settings: ##########################################################
    # set frames per second of the game (not really important since there aren't any animations however it is needed for the game clock)
    fps = 25

    ################################################
    main_bg = pygame.image.load("./img/main_bg.png")
    # ensure the image covers the whole window by setting its width and height to the screen's resolution
    main_bg = pygame.transform.scale(main_bg, (w, h))

    menuBg = pygame.image.load("./img/menu_bg.png")
    menuBg = pygame.transform.scale(menuBg, (w, h))
    lionImg = pygame.image.load("./img/lion.png")
    # lionImg = = pygame.transform.scale(menuBg, (w, h))
    batImg = pygame.image.load("./img/bats.png")
    batImg = pygame.transform.scale(batImg, (500, 500))
    gradientBg = pygame.image.load("./img/gradient_bg.jpg")
    gradientBg = pygame.transform.scale(gradientBg, (w, h))

    clock = pygame.time.Clock()  # create game clock

    # GAME ACTIVE ################################## delete after development finished
    # mainMenuActive = False
    # gameActive = True

    # Menu Active, and the game is not currently running on startup
    mainMenuActive = True
    gameActive = False

    showLionDeathText = False
    showBatMoveText = False
    # Text needed for the main menu
    # Create instances of a TextObj which is used to display text on the screen (in this case the buttons and title text)
    titleText = TextObj("title", w/14, (h/4)-20, "SAMSON", w, h)
    playBtn = TextObj("play", w/14, (h/4)+62, "Play", w, h)
    rulesBtn = TextObj("rules", w/14, (h/4)+140, "Rules", w, h)
    leaderboardBtn = TextObj("leaderboard",w/14, (h/4)+230, "Leaderboard", w,h)
    controlsBtn = TextObj("ctrl", w/14, (h/4)+320, "Controls", w, h)
    quitBtn = TextObj("quit", w/14, (h/4)+410, "Quit", w, h)

    backBtn = TextObj("back", (w/2)-50, h-150, "Back", w, h)

    versionText = TextObj('version', 92*w/100, h-50, str(__version__), w, h)
    # A list with all the menu selections
    # menuSelections = [playBtn, rulesBtn, quitBtn]
    menuSelections = [playBtn, rulesBtn, leaderboardBtn, controlsBtn, quitBtn]

    currMenuSelection = playBtn
    initGame = True
    
    leaderboard = Leaderboard(screen, arcadeFontMedium, arcadeFontSmall, gradientBg)
    controlsScreen = Controls(screen, arcadeFontMedium, arcadeFontSmall, gradientBg)
    rulesScreen = Rules(screen, arcadeFontMedium, arcadeFontExtraSmall, gradientBg)

####################################################################################
    while running:  # while the game is running,

        if initGame:  # we need to initialise the game when we first start it up or restart. This just runs in the background while the menu is open so the game is already created when the user clicks play
            print("---------------------------GAME STARTED-----------------------------")
            score = 0
            turns = 0
            batsNum = 2  # number of bats to be generated
            lionNum = 2  # number of lions to be generated
            resultAdded = False
            # list of nodes in the graph that are occupied (by either player or hazards)
            filledNodes = []
            playerInstance = player()  # create an instance of the player class
            print(f"{playerInstance.pos = }")
            # add the player's starting position to the list of filled nodes (so we don't try to add hazards onto it.)
            filledNodes.append(playerInstance.pos)

            wumpusInstance = wumpus()  # create an instance of the wumpus class
            # make sure the wumpus is not on the same node as another object in the game(as the player)
            while wumpusInstance.pos in filledNodes:
                wumpusInstance.pos == getRandomNode()
            filledNodes.append(wumpusInstance.pos)

            currNode = playerInstance.pos
            # print(f"initial {currNode = }")
            bats = []  # empty list fo
            lions = []
            # wumpusNum = 1
            # wumpusNodes = []
            playVictoryMusic = True

            # for w in range(wumpusNum):
            #     wumpusInstance = wumpus()
            #     wumpusNodes.append(wumpusInstance.pos)
            # used for testing to keep track of the locations of the lions (for debugging)
            batNodes = []
            # used for testing to keep track of the locations of the lions (for debugging)
            lionNodes = []

            # create the specified amount bat instances and add them to the bat list
            for b in range(batsNum):
                batInstance = bat()  # create new bat instance

                # make sure the bats is not on the same node as another object in the game(as the player)
                while batInstance.pos in filledNodes:
                    # set the instances position to another random node
                    batInstance.pos = getRandomNode()
                bats.append(batInstance)  # add the bat to the list of bats
                # add the bat's position to the list of filled nodes
                filledNodes.append(batInstance.pos)
                batNodes.append(batInstance.pos)

            # create the specified amount lion instances and add them to the lion list
            for p in range(lionNum):
                lionInstance = Lion()  # create new bat instance

                # make sure the wumpus is not on the same node as another object in the game(as the player)
                while lionInstance.pos in filledNodes:
                    # set the instances position to another random node
                    lionInstance.pos = getRandomNode()
                lions.append(lionInstance)  # add the lion to the list of lions
                # add the lion's position to the list of filled nodes
                filledNodes.append(lionInstance.pos)
                lionNodes.append(lionInstance.pos)

            print(f"{filledNodes = }")
            print(f"{wumpusInstance.pos = }")

            print(f"{lionNodes = }")
            print(f"{batNodes = }")

            wumpusDistance = min(findHazard(graph, currNode, wump.pos) for wump in [  # min depth of all the possible paths to the wumpus to find the shortest distance
                                 wumpusInstance])  # returns wumpus distance from spawn.
            lionDistance = min([findHazard(graph, currNode, lion.pos)  # returns lion distance from spawn. (for all lions)
                              for lion in lions])
            batDistance = min([findHazard(graph, currNode, bat.pos)  # returns bat distance from spawn. (for all lions)
                              for bat in bats])

            colObj = playerInstance.detectHazardCollision(  # Check if the player is currently in the same node as a hazard
                currNode, wumpusInstance, lions, bats)
            if colObj != "null":
                # raise an exception since this shouldn't have happened, since the player shouldn't be in the same node as a hazard and show the object the player collided with.
                # colObj is the object the player collided with
                raise ValueError(f"{colObj = }")

            charges = 5  # amount of charges that the player has (for the game)
            # Set the variable to None so it can be used later to check if the player is charging.
            # set the variable to None so it can be used later to check if the player is charging.
            isCharging = None
            # Set the variable to None so it can be used later to check if the player is charging.
            # set the variable to None so it can be used when the player has attempted a charge
            chargeRes = None

            gameOver = False  # Set to false since the game hasn't ended
            endCause = ""  # empty string to start with.
            menuSound.play()  # play the main menu soundtrack
            # menuSound.play() # play the sound

            # Reset the menu settings that may have been altered and ensure that the game doesn't keep re-running
            initGame = False
            menuPlay = False
            menuRules = False
            menuControls = False
            menuLeaderboard = False
            menuQuit = False
            # end of main menu
            leaderboardOpen = False
            controlsOpen = False
            rulesOpen = False

        if gameOver:  # when the game has ended
            score = (1/turns)*10000 # calculate the score by doing inverse of the amt of turns taken to defeat wumpus (so that less turns = higher scores then multiply by 10000 to get a bigger number
            if resultAdded == False:
                leaderboard.AddResult(score)  # add the score to the leaderboard
                resultAdded = True
            msg2 = "error"  # default message to display
            msg1 = "shoot"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # close when x button hit
                    running = False
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    pygame.mixer.pause()
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        pygame.quit()
                    else:
                        # pygame.mixer.pause()
                        initGame = True
                        mainMenuActive = True
                        gameOver = False
                        gameActive = False
            if endCause == "slayed":
                msg1 = "Congratulations!"
                msg2 = f"You have won the game with a score of {int(score)}!"
                if playVictoryMusic:
                    victorySound.play()
                    playVictoryMusic = False
            else:
                msg1 = "Game Over!"

                if endCause == "charge":
                    msg2 = "You ran out of charges"

                elif endCause == "lion":
                    msg2 = "A Mystical lion appeared out of nowhere and killed you"
                    screen.blit(lionImg, (1,1))
                elif endCause == "wumpus":
                    msg2 = "You accidentally stumbled upon an army of Philistines! You died!"
                else:
                    raise ValueError(f"{endCause = }")
            msg3 = "Press any button to restart"
            text1 = arcadeFontMedium.render(msg1, True, (255, 255, 255))
            text2 = arcadeFontSmall.render(msg2, True, (255, 255, 255))
            text3 = arcadeFontSmall.render(msg3, True, (255, 255, 255))
            screen.fill((0, 0, 0))
            screen.blit(text1, (100, 300))
            screen.blit(text2, (100, 600))  # draw on screen
            screen.blit(text3, (100, 900))

            # initGame = True
            # mainMenuActive = True

        if mainMenuActive:
              
            pygame.mixer.unpause() #unpause the mixer so music starts playing again
            screen.blit(menuBg, (1, 1)) # blit the menu BG image to the screen first (so FG gets drawn over it)

            titleText.draw(arcadeFont60, screen, (0, 0, 0))
            playBtn.draw(arcadeFont60, screen)
            rulesBtn.draw(arcadeFont60, screen)
            leaderboardBtn.draw(arcadeFont60, screen)
            controlsBtn.draw(arcadeFont60, screen)
            quitBtn.draw(arcadeFont60, screen)
            # leaderboardBtn.draw(arcadeFontMedium, screen)

            versionText.draw(arcadeFontSmall, screen)

            selectionRectBorder = pygame.draw.rect(screen, (255, 60, 5), pygame.Rect(
                (w/15)-5, currMenuSelection.y-10, 475, 80), 1, 8)
            selectionRectFill = pygame.gfxdraw.box(screen, pygame.Rect(
                (w/15)-5, currMenuSelection.y-10, 475, 79), (0, 0, 0, 7))
            mousePos = pygame.mouse.get_pos()

            for btn in menuSelections:
                if btn.Hover(mousePos):
                    # print(btn.name, "hovered")
                    currMenuSelection = btn

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # close when x button hit
                    running = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    try:
                        if backBtn.Hover(mousePos):
                            menuRules = False
                            menuControls = False
                            menuLeaderboard = False
                    except:
                        pass # means that the back button isn't active yet
                        
                    for btn in menuSelections:
                        if btn.Hover(mousePos):
                            if btn.name == "play":
                                menuPlay = True
                            elif btn.name == "rules":
                                menuRules = True
                            elif btn.name == "leaderboard":
                                menuLeaderboard = True
                            elif btn.name == "ctrl":
                                menuControls = True
                            elif btn.name == "quit":
                                menuQuit = True
                    # if rect1.collidepoint(pygame.mouse.get_pos()):
                    #     print("Mouse clicked on the rect")

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        pygame.quit()

                    if event.key == pygame.K_DOWN:
                        if menuSelections.index(currMenuSelection) + 1 == len(menuSelections):
                            currMenuSelection = menuSelections[0]
                        else:
                            currMenuSelection = menuSelections[menuSelections.index(
                                currMenuSelection) + 1]
                        # print(currMenuSelection.name)
                    if event.key == pygame.K_UP:
                        if menuSelections.index(currMenuSelection) + -1 == 0:
                            currMenuSelection = menuSelections[0]
                        else:
                            currMenuSelection = menuSelections[menuSelections.index(
                                currMenuSelection) - 1]

                    if event.key == pygame.K_RETURN:
                        if currMenuSelection.name == "play":
                            menuPlay = True

                        elif currMenuSelection.name == "rules":
                            menuRules = True
                        
                        elif currMenuSelection.name == "ctrl":
                            menuControls = True

                        elif currMenuSelection.name == "leaderboard":
                            menuLeaderboard = True
                        elif currMenuSelection.name == "quit":
                            menuQuit = True

                        if leaderboardOpen: # draw over main menu
                            menuLeaderboard = False
                            leaderboardOpen = False

                        elif controlsOpen: # draw over main menu
                            menuControls = False
                            controlsOpen = False

                        elif rulesOpen: # draw over main menu
                            menuRules = False
                            rulesOpen = False
            if menuPlay:
                pygame.mixer.pause()
                mainMenuActive = False
                gameActive = True
                menuPlay = False

            elif menuRules:
                rulesOpen = True
                rulesScreen.Show()
                backBtn.draw(arcadeFont60, screen, (0,0,0))

            elif menuControls:
                controlsOpen = True
                controlsScreen.Show()
                backBtn.draw(arcadeFont60, screen, (0,0,0)) 

            elif menuLeaderboard:
                leaderboardOpen = True
                leaderboard.Show()
                backBtn.draw(arcadeFont60, screen, (0,0,0))

            elif menuQuit:
                running = False
                pygame.quit()
        


################################################################## GAME ACTIVE
        elif gameActive:
            if charges <= 0:
                endCause = "charge"
                gameActive = False
                gameOver = True
            screen.blit(main_bg, (1, 1))

            # screen.fill(bgColour)  # fill before anything else
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # close when x button hit
                    running = False
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        pygame.quit()
                    if event.key == pygame.K_LSHIFT:
                        isCharging = True

                    if event.key == pygame.K_LEFT:
                        turns += 1
                        if isCharging:
                            print("charge left")
                            charges -= 1
                            chargeRes = Charge(
                                0, currNode, charges, wumpusInstance.pos, graph)

                        currNode, wumpusDistance, lionDistance, batDistance = validInputReceived(
                            graph,
                            currNode,
                            0,
                            wumpusInstance,
                            lions,
                            bats,
                            playerInstance,
                        )

                    if event.key == pygame.K_UP:
                        turns += 1
                        if isCharging:
                            print("charge up")
                            charges -= 1
                            chargeRes = Charge(
                                1, currNode, charges, wumpusInstance.pos, graph)

                        currNode, wumpusDistance, lionDistance, batDistance = validInputReceived(
                            graph,
                            currNode,
                            1,
                            wumpusInstance,
                            lions,
                            bats,
                            playerInstance,
                        )

                    if event.key == pygame.K_RIGHT:
                        turns += 1
                        if isCharging:
                            print("charge right")
                            charges -= 1
                            chargeRes = Charge(
                                2, currNode, charges, wumpusInstance.pos, graph)

                        currNode, wumpusDistance, lionDistance, batDistance = validInputReceived(
                            graph,
                            currNode,
                            2,
                            wumpusInstance,
                            lions,
                            bats,
                            playerInstance)
                    if isCharging:
                        if chargeRes == False:
                            print("charge FAILED")
                            isCharging = None
                            chargeRes = None

                        elif chargeRes == True:
                            endCause = "slayed"
                            gameActive = False
                            gameOver = True
                    else:
                        
                        colObj = playerInstance.detectHazardCollision(
                            currNode, wumpusInstance, lions, bats)

                    if colObj != "null":

                        startTime = time.time()
                        if colObj.type == "wumpus":
                            endCause = "wumpus"
                            print(f"just hit the WUMPUS at {colObj.pos}")
                            gameActive = False
                            gameOver = True

                        elif colObj.type == "lion":
                            
                            print(f"just hit a LION at {colObj.pos}")
                            endCause = "lion"
                            gameActive = False
                            gameOver = True

                        elif colObj.type == "bat":
                            print(f"just hit a BAT at {colObj.pos}")
                            currNode = getRandomNode()
                            while currNode in filledNodes:
                                currNode = getRandomNode()
                            # batTextTime = time.time()
                            showBatMoveText = True

            if showBatMoveText:
                pass
                showTimedText(400, 100, 1, batImg, fontColour,
                              font, screen, startTime)
            else:
                showLionDeathText = False
                showBatMoveText = False

            hazardDistance = {'wumpusDistance': wumpusDistance,
                              'lionDistance': lionDistance, 'batDistance': batDistance}

            showText(currNode, w, h, fontColour, arcadeFontSmall,
                     screen, graph, hazardDistance, charges)

        frameCount += fps  # delete later unless i actually use it
        clock.tick(fps)
        pygame.display.update()
#   except Exception as e:
#       print(f"ERROR {e}")


if __name__ == "__main__":
    print('Author: ' + __author__)
    print('License: ' + __license__)
    print('Version: ' + __version__)
    print('Email: ' + __email__)
    print('Course: ' + __course__)
    print('Date: ' + __date__)
    print('Description: ' + __description__)
    print(__info__)
    print("\n")
    print("Python " + __pyver__)
    print("Pygame " + __pygamever__)
    print('# ' + '=' * 78)
    main()
