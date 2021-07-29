__author__ = 'Noah Vendrig'
__license__ = 'MIT'  # copy of the license available @ https://prodicus.mit-license.org/
__version__ = '2.5'
__email__ = 'noah.vendrig@education.nsw.gov.au'
__github__ = "github.com/noahvendrig"  # @noahvendrig
__course__ = 'Software Design and Development'
__date__ = '30/07/2021'
__description__ = '\'Samson\' is a Modern Recreation of text-based adventure game Hunt the Wumpus (1973)'
__specifications__ = "noahvendrig.com/#about"  # specifications available here
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


class pit(hazard):
    def __init__(self):
        hazard.__init__(self)
        self.type = "pit"


class bat(hazard):
    def __init__(self):
        hazard.__init__(self)
        self.type = "bat"


class player:
    def __init__(self):
        self.type = "player"
        self.pos = getRandomNode()

    def detectHazardCollision(self, playerPos, wumpusInstance, pits, bats):
        if playerPos in [wumpusInstance.pos]:
            return wumpusInstance

        for pit in pits:
            if playerPos == pit.pos:
                return pit

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


def validInputReceived(graph, currNode, keyNum, wumpusInstance, pits, bats, playerInstance):

    currNode = changeNode(graph, currNode, keyNum)
    wumpusDist = min(findHazard(graph, currNode, wump.pos)
                     for wump in [wumpusInstance])  # change to wumpus list
    # wumpusDist = findHazard(graph, currNode, wumpusInstance.pos)
    pitDist = min([findHazard(graph, currNode, pit.pos) for pit in pits])
    batDist = min([findHazard(graph, currNode, bat.pos) for bat in bats])
    # print(f"{pitDist = }")
    # print(f"{batDist = }")
    return currNode, wumpusDist, pitDist, batDist


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
                screen.blit(distanceTxt, (x_distTxt, displayAdjustment))
                displayAdjustment += 125

            elif key == "pitDistance":
                # print(f"{key} = {hazardDistance[key]}")
                distanceTxt = font.render(
                    "THERE IS A PIT NEARBY",
                    True,
                    fontColour,  # finds integers in the string e.g. "19" in "n19" to display
                )

                # draw on screen
                screen.blit(distanceTxt, (x_distTxt, displayAdjustment))
                displayAdjustment += 125

            elif key == "batDistance":
                # print(f"{key} = {hazardDistance[key]}")
                distanceTxt = font.render(  # "Soft purrs can be heard from a nearby cave..."
                    "You can hear bats nearby",
                    True,
                    fontColour,  # finds integers in the string e.g. "19" in "n19" to display
                )

                # draw on screen
                screen.blit(distanceTxt, (x_distTxt, displayAdjustment))
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


def pitDeath(fontColour, font, screen):
    # deathTxt = font.render("YOU FELL INTO A PIT",True,fontColour)
    # screen.blit(deathTxt, (200, 350))  # draw on screen
    showTimedText(300, 400, 5, "YOU FELL INTO A PIT LO IT WORKS",
                  fontColour, font, screen)


def showBat(screen, batImg):
    screen.blit(batImg, (400, 100))
    pygame.display.update()


class TextObj():
    def __init__(self, name, x, y, txt, w, h):
        self.x = x
        self.y = y
        self.txt = txt
        self.w = w
        self.h = h
        self.name = name

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

    batSound = pygame.mixer.Sound("./audio/bat.mp3")
    wumpusSound = pygame.mixer.Sound("./audio/wumpus.mp3")
    # pitSound = pygame.mixer.music("./audio/pit.mp3")
    pitSound = pygame.mixer.Sound("./audio/w.wav")
    menuSound = pygame.mixer.Sound("./audio/menu.mp3")
    # allow for multiple channle use, so that sounds can be played over each other
    pygame.mixer.set_num_channels(5)
    # pitSound.play()
    # wumpusSound.play()

    # arialFont = pygame.font.SysFont("Arial", 30)
    frameCount = 0

    user32 = ctypes.windll.user32
    screenSize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(
        1)  # get the resolution of the user's computer
    if screenSize[0]/screenSize[1] != 16/9:
        # TODO: make the game window size shrink so that a 16:9 ratio is maintained but fill the excess with a black background
        w = screenSize[0]
        h = screenSize[1]
    else:
        w = screenSize[0]
        h = screenSize[1]

    # w = 1600
    # h = 500

    bgColour = (255, 255, 255)
    running = True

    pygame.display.set_caption("Hunt the Wumpus")
    screen = pygame.display.set_mode((w, h))
    fontColour = (0, 0, 0)

    # font = ("./arial.tff", 32)
    font = pygame.font.Font("freesansbold.ttf", 32)

    arcadeFontMedium = pygame.font.Font("font/arcade.ttf", (int((w+h)/45)))
    arcadeFontSmall = pygame.font.Font("font/arcade.ttf", (int((w+h)/100)))
    # currNode = "n1"  # set the starting node
    # settings: ##########################################################
    fps = 25

    ################################################
    main_bg = pygame.image.load("./img/main_bg.png")
    main_bg = pygame.transform.scale(main_bg, (w, h))

    menuBg = pygame.image.load("./img/menu_bg.png")
    menuBg = pygame.transform.scale(menuBg, (w, h))

    batImg = pygame.image.load("./img/bats.png")
    batImg = pygame.transform.scale(batImg, (500, 500))

    # print(f"{type(batImg) = }")

    clock = pygame.time.Clock()

    # GAME ACTIVE ################################## delete after development finished
    # mainMenuActive = False
    # gameActive = True

    # Menu Active
    mainMenuActive = True
    gameActive = False

    showPitDeathText = False
    showBatMoveText = False

    titleText = TextObj("title", w/14, (h/4)-20, "SAMSON", w, h)
    playBtn = TextObj("play", w/14, (h/4)+62, "Play", w, h)
    optBtn = TextObj("opt", w/14, (h/4)+152, "Options", w, h)
    # leaderboardBtn = TextObj("leaderboard",w/14, (h/4)+242, "Leaderboard", w,h)
    quitBtn = TextObj("quit", w/14, (h/4)+242, "Quit", w, h)  # 322

    versionText = TextObj('version', 92*w/100, h-50, str(__version__), w, h)
    menuSelections = [playBtn, optBtn, quitBtn]
    # menuSelections = [playBtn, optBtn, leaderboardBtn, quitBtn]

    currMenuSelection = playBtn
    initGame = True
####################################################################################
    while running:

        if initGame:
            print("---------------------------GAME STARTED-----------------------------")
            batsNum = 2
            pitNum = 2

            filledNodes = []
            playerInstance = player()
            print(f"{playerInstance.pos = }")
            filledNodes.append(playerInstance.pos)

            wumpusInstance = wumpus()
            while wumpusInstance.pos in filledNodes:
                wumpusInstance.pos == getRandomNode()
            filledNodes.append(wumpusInstance.pos)

            currNode = playerInstance.pos
            # print(f"initial {currNode = }")
            bats = []
            pits = []
            # wumpusNum = 1
            # wumpusNodes = []

            # for w in range(wumpusNum):
            #     wumpusInstance = wumpus()
            #     wumpusNodes.append(wumpusInstance.pos)
            batNodes = []  # delete later
            pitNodes = []  # delete later

            for b in range(batsNum):
                batInstance = bat()
                while batInstance.pos in filledNodes:
                    batInstance.pos = getRandomNode()
                bats.append(batInstance)
                filledNodes.append(batInstance.pos)
                batNodes.append(batInstance.pos)

            for p in range(pitNum):
                pitInstance = pit()
                while pitInstance.pos in filledNodes:
                    pitInstance.pos = getRandomNode()
                pits.append(pitInstance)
                filledNodes.append(pitInstance.pos)
                pitNodes.append(pitInstance.pos)

            print(f"{filledNodes = }")
            print(f"{wumpusInstance.pos = }")

            print(f"{pitNodes = }")  # delete later
            print(f"{batNodes = }")  # delete later

            wumpusDistance = min(findHazard(graph, currNode, wump.pos) for wump in [
                                 wumpusInstance])  # calculate initial wumpus distance from spawn
            pitDistance = min([findHazard(graph, currNode, pit.pos)
                              for pit in pits])
            batDistance = min([findHazard(graph, currNode, bat.pos)
                              for bat in bats])

            colObj = playerInstance.detectHazardCollision(
                currNode, wumpusInstance, pits, bats)
            if colObj != "null":
                raise Exception(f"{colObj = }")

            charges = 5
            isCharging = None
            chargeRes = None

            gameOver = False
            endCause = ""
            menuSound.play()  # play the sound
            # menuSound.play() # play the sound

            initGame = False

            menuPlay = False
            menuOpt = False
            menuQuit = False
            # end

        # leftMouse, middleMouse, rightMouse = pygame.mouse.get_pressed()
        # print(leftMouse, middleMouse, rightMouse)
        if gameOver:
            msg2 = "error"
            msg1 = "shoot"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # close when x button hit
                    running = False
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        pygame.quit()
                    else:
                        initGame = True
                        mainMenuActive = True
                        gameOver = False
                        gameActive = False
            if endCause == "slayed":
                msg1 = "Congratulations!"
                msg2 = "You have won the game!"
            else:
                msg1 = "Game Over!"

                if endCause == "charge":
                    msg2 = "You ran out of charges"

                elif endCause == "pit":
                    msg2 = "You fell into a pit and died"
                elif endCause == "wumpus":
                    msg2 = "You accidentally stumbled upon an army of Philistines,\nand couldn't make it out"
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
            pygame.mixer.unpause()
            screen.blit(menuBg, (1, 1))

            titleText.draw(arcadeFontMedium, screen, (0, 0, 0))
            playBtn.draw(arcadeFontMedium, screen)
            optBtn.draw(arcadeFontMedium, screen)
            quitBtn.draw(arcadeFontMedium, screen)
            # leaderboardBtn.draw(arcadeFontMedium, screen)

            versionText.draw(arcadeFontSmall, screen)

            selectionRectBorder = pygame.draw.rect(screen, (255, 84, 5), pygame.Rect(
                (w/15)-5, currMenuSelection.y+2, 415, 80), 1, 8)
            pygame.gfxdraw.box(screen, pygame.Rect(
                (w/15)-5, currMenuSelection.y+2, 414, 79), (0, 0, 0, 7))
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
                    for btn in menuSelections:
                        if btn.Hover(mousePos):
                            if btn.name == "play":
                                menuPlay = True
                            elif btn.name == "opt":
                                menuOpt = True
                            elif btn.name == "quit":
                                menuQuit = True
                    # if rect1.collidepoint(pygame.mouse.get_pos()):
                    #     print("Mouse clicked on the rect")

                if event.type == pygame.KEYDOWN:
                    # if event.key == pygame.K_ESCAPE:
                    #     running = False
                    #     pygame.quit()

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

                        if currMenuSelection.name == "opt":
                            menuOpt = True
                        # if currMenuSelection.name == "leaderboard":
                        #     pass
                        if currMenuSelection.name == "quit":
                            menuQuit = True
            if menuPlay:
                pygame.mixer.pause()
                mainMenuActive = False
                gameActive = True
                menuPlay = False
            if menuOpt:
                pass
            if menuQuit:
                running = False
                pygame.quit()

        elif gameActive:
            if charges <= 0:
                endCause = "wumpus"
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
                        if isCharging:
                            print("charge left")
                            charges -= 1
                            chargeRes = Charge(
                                0, currNode, charges, wumpusInstance.pos, graph)

                        currNode, wumpusDistance, pitDistance, batDistance = validInputReceived(
                            graph,
                            currNode,
                            0,
                            wumpusInstance,
                            pits,
                            bats,
                            playerInstance,
                        )

                    if event.key == pygame.K_UP:
                        if isCharging:
                            print("charge up")
                            charges -= 1
                            chargeRes = Charge(
                                1, currNode, charges, wumpusInstance.pos, graph)

                        currNode, wumpusDistance, pitDistance, batDistance = validInputReceived(
                            graph,
                            currNode,
                            1,
                            wumpusInstance,
                            pits,
                            bats,
                            playerInstance,
                        )

                    if event.key == pygame.K_RIGHT:

                        if isCharging:
                            print("charge right")
                            charges -= 1
                            chargeRes = Charge(
                                2, currNode, charges, wumpusInstance.pos, graph)

                        currNode, wumpusDistance, pitDistance, batDistance = validInputReceived(
                            graph,
                            currNode,
                            2,
                            wumpusInstance,
                            pits,
                            bats,
                            playerInstance)
                    if isCharging:
                        if chargeRes == False:
                            print("charge FAILED")
                            isCharging = None
                            chargeRes = None

                        elif chargeRes == True:
                            endCause == "slayed"
                            gameActive = False
                            gameOver = True
                    else:
                        colObj = playerInstance.detectHazardCollision(
                            currNode, wumpusInstance, pits, bats)

                    if colObj != "null":
                        startTime = time.time()
                        if colObj.type == "wumpus":
                            endCause = "wumpus"
                            print(f"just hit the WUMPUS at {colObj.pos}")
                            gameActive = False
                            gameOver = True

                        elif colObj.type == "pit":
                            print(f"just hit a PIT at {colObj.pos}")
                            endCause = "pit"
                            gameActive = False
                            gameOver = True
                            # initGame = True
                            # mainMenuActive = True
                            # gameActive = False

                        elif colObj.type == "bat":
                            print(f"just hit a BAT at {colObj.pos}")
                            currNode = getRandomNode()
                            while currNode in filledNodes:
                                currNode = getRandomNode()
                            # batTextTime = time.time()
                            showBatMoveText = True

            if showPitDeathText:
                showTimedText(400, 300, 10, "just hit a PIT oof",
                              fontColour, font, screen, startTime)

            elif showBatMoveText:
                pass
                showTimedText(400, 100, 1, batImg, fontColour,
                              font, screen, startTime)
            else:
                showPitDeathText = False
                showBatMoveText = False

            hazardDistance = {'wumpusDistance': wumpusDistance,
                              'pitDistance': pitDistance, 'batDistance': batDistance}

            showText(currNode, w, h, fontColour, font,
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
    print("\n")
    print("Python " + __pyver__)
    print("Pygame " + __pygamever__)
    print('# ' + '=' * 78)
    main()
