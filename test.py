
__author__ = 'Noah Vendrig'
__license__ = 'MIT' # copy of the license available @ https://prodicus.mit-license.org/
__version__ = '1.0.1'
__email__ = 'noah.vendrig@education.nsw.gov.au'
__github__ = "github.com/noahvendrig" # @noahvendrig
__course__ = 'Software Design and Development'
__date__ = '10/07/2021'
__description__ = 'Modern Recreation of text-based adventure game Hunt the Wumpus (1973)'
__specifications__ = "noahvendrig.com/#about" #specifications available here

# ====================================== Imports ======================================
import pygame  # pygame 2.0.1 (SDL 2.0.14, Python 3.8.10) # after activating conda env run the following in cmd: 'pip install pygame'
from sys import exit, float_repr_style
import numpy
import random
from pygame.locals import *
import re
import time
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
        text= content

    if time.time() - startTime < duration: # while it hasnt been duration in seconds
        screen.blit(text, (x, y))  # draw on screen
        pygame.display.update()
    

def validInputReceived(graph, currNode, keyNum, wumpusInstance, pits, bats, playerInstance):

    currNode = changeNode(graph, currNode, keyNum)
    wumpusDist = min(findHazard(graph, currNode, wump.pos) for wump in [wumpusInstance]) # change to wumpus list
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


def showText(currNode, w, h, fontColour, font, screen, graph, hazardDistance):
    roomL_X = (w * 0.1) - 100
    roomL_Y = h / 2
    roomM_X = (w / 2) - 50
    roomM_Y = h * 0.1
    roomR_X = (w * 0.9) - 25
    roomR_Y = h / 2

    currRoom_X = (w / 2) - 50
    currRoom_Y = h / 2

    # DISTANCE
    
    for key in hazardDistance:
        if hazardDistance[key] == 1:
            # print(f"{key} = {hazardDistance[key]}")
            if key == "wumpusDistance":
                
                distanceTxt = font.render(
                        "THE WUMPUS IS NEARBY",
                        True,
                        fontColour,  # finds integers in the string e.g. "19" in "n19" to display
                    )
                # distanceTxt = font.render(
                #     f"{key} is %s nodes away" % hazardDistance[key],
                #     True,
                #     fontColour,  # finds integers in the string e.g. "19" in "n19" to display
                # )
                screen.blit(distanceTxt, (300, 400))  # draw on screen
            if key == "pitDistance":
            # print(f"{key} = {hazardDistance[key]}")
                distanceTxt = font.render(
                    "THERE IS A PIT NEARBY",
                    True,
                    fontColour,  # finds integers in the string e.g. "19" in "n19" to display
                )
                screen.blit(distanceTxt, (300, 500))  # draw on screen
            if key == "batDistance":
            # print(f"{key} = {hazardDistance[key]}")
                distanceTxt = font.render(
                    "THERE ARE BATS NEARBY",
                    True,
                    fontColour,  # finds integers in the string e.g. "19" in "n19" to display
                )
                screen.blit(distanceTxt, (200, 350))  # draw on screen

    currRoom_Txt = font.render(
        "Room " + (re.findall("[0-9]+", currNode)[0]),
        True,
        fontColour,  # finds integers in the string e.g. "19" in "n19" to display
    )
    screen.blit(currRoom_Txt, (currRoom_X, currRoom_Y))  # draw on screen

    RoomL_Txt = font.render(
        "Room " + (re.findall("[0-9]+", graph[currNode][0])[0]),
        True,
        fontColour,  # finds integers in the string e.g. "19" in "n19" to display
    )
    screen.blit(RoomL_Txt, (roomL_X, roomL_Y))  # draw on screen

    RoomM_Txt = font.render(
        "Room " + (re.findall("[0-9]+", graph[currNode][1])[0]),
        True,
        fontColour,  # finds integers in the string e.g. "19" in "n19" to display
    )
    screen.blit(RoomM_Txt, (roomM_X, roomM_Y))  # draw on screen

    RoomR_Txt = font.render(
        "Room " + (re.findall("[0-9]+", graph[currNode][2])[0]),
        True,
        fontColour,  # finds integers in the string e.g. "19" in "n19" to display
    )
    screen.blit(RoomR_Txt, (roomR_X, roomR_Y))  # draw on screen


def getRandomNode():
    num = random.randint(1, 20)
    node = "n" + str(num)
    return node


def wumpusDeath(fontColour, font, screen):
    deathTxt = font.render("YOU GOT KILLED BY THE WUMPUS",True,fontColour)
    screen.blit(deathTxt, (200, 350))  # draw on screen
    pass


def pitDeath(fontColour, font, screen):
    # deathTxt = font.render("YOU FELL INTO A PIT",True,fontColour)
    # screen.blit(deathTxt, (200, 350))  # draw on screen
    showTimedText(300, 400, 5, "YOU FELL INTO A PIT LO IT WORKS", fontColour, font, screen)


def showBat(screen, batImg):
    screen.blit(batImg, (400, 100))
    pygame.display.update()

def registerSelection(currentSelection):
    pass

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

    batSound = pygame.mixer.Sound("./audio/bat.mp3")
    wumpusSound = pygame.mixer.Sound("./audio/wumpus.mp3")
    # pitSound = pygame.mixer.music("./audio/pit.mp3")
    pitSound = pygame.mixer.Sound("./audio/w.wav")
    pygame.mixer.set_num_channels(5)
    # pitSound.play()
    # wumpusSound.play()

    # arialFont = pygame.font.SysFont("Arial", 30)
    frameCount = 0

    w = 1800
    h = 900

    bgColour = (255, 255, 255)
    running = True

    pygame.display.set_caption("Hunt the Wumpus")
    screen = pygame.display.set_mode((w, h))
    fontColour = (0, 0, 0)

    # font = ("./arial.tff", 32)
    font = pygame.font.Font("freesansbold.ttf", 32)

    # currNode = "n1"  # set the starting node
    # settings: ##########################################################
    fps = 25
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
    batNodes = []  #################################### delete later
    pitNodes = []  #################################### delete later

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

    print(f"{pitNodes = }")  #################################### delete later
    print(f"{batNodes = }")  #################################### delete later

    ################################################
    bgImg = pygame.image.load("./img/bg.jpg")
    bgImg = pygame.transform.scale(bgImg, (w, h))

    batImg = pygame.image.load("./img/bats.png")
    batImg = pygame.transform.scale(batImg, (500, 500))

    # print(f"{type(batImg) = }")

    clock = pygame.time.Clock()

    wumpusDistance = min(findHazard(graph, currNode, wump.pos) for wump in [wumpusInstance])  # calculate initial wumpus distance from spawn
    pitDistance = min([findHazard(graph, currNode, pit.pos) for pit in pits])
    batDistance = min([findHazard(graph, currNode, bat.pos) for bat in bats])

    colObj = playerInstance.detectHazardCollision(currNode, wumpusInstance, pits, bats)
    if colObj != "null":
        raise Exception(f"{colObj = }")

    #GAME ACTIVE ################################## delete after development finished
    mainMenuActive = False
    gameActive = True

    #Menu Active 
    # mainMenuActive = True
    # gameActive = False

    showPitDeathText = False
    showBatMoveText = False

    while running:
        
        # leftMouse, middleMouse, rightMouse = pygame.mouse.get_pressed()
        # print(leftMouse, middleMouse, rightMouse)

        if mainMenuActive:
            screen.blit(bgImg, (1, 1))
            rect1 = pygame.draw.rect(screen,(0,0,255),(200,150,100,50))
            
            currentSelection = "startBtn"
            
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:           
                    if rect1.collidepoint(pygame.mouse.get_pos()):
                        print("Mouse clicked on the rect")

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        pygame.quit()
                    if event.key == pygame.K_RETURN:
                        print("enter hit")
                        registerSelection(currentSelection) #do something since the current selection has been confirmed e.g start game if that option is selected
        elif gameActive:
            
            screen.blit(bgImg, (1, 1))
            
            # screen.fill(bgColour)  # fill before anything else
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # close when x button hit
                    running = False
                    pygame.quit()
                

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        pygame.quit()

                    if event.key == pygame.K_LEFT:
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
                        currNode, wumpusDistance, pitDistance, batDistance = validInputReceived(
                            graph,
                            currNode,
                            2,
                            wumpusInstance,
                            pits,
                            bats,
                            playerInstance,
                        )

                    colObj = playerInstance.detectHazardCollision(
                        currNode, wumpusInstance, pits, bats
                    )

                    if colObj != "null":
                        startTime = time.time()
                        if colObj.type == "wumpus":
                            print(f"just hit the WUMPUS at {colObj.pos}")
                            wumpusDeath(fontColour, font, screen)

                        elif colObj.type == "pit":
                            print(f"just hit a PIT at {colObj.pos}")
                            # pitDeath(fontColour, font, screen)
                            showPitDeathText = True
                            # startTime = time.time()

                        elif colObj.type == "bat":
                            print(f"just hit a BAT at {colObj.pos}")
                            currNode = getRandomNode()
                            # batTextTime = time.time()
                            showBatMoveText = True

            if showPitDeathText:
                showTimedText(400, 300, 10, "just hit a PIT oof", fontColour, font, screen, startTime)
            
            elif showBatMoveText:
                showTimedText(400, 100, 1, batImg, fontColour, font, screen, startTime)
            else:
                showPitDeathText = False
                showBatMoveText = False
                
            hazardDistance = {'wumpusDistance': wumpusDistance, 'pitDistance': pitDistance, 'batDistance': batDistance}

            showText(currNode, w, h, fontColour, font, screen, graph, hazardDistance)
        
        frameCount += fps #delete later unless i actually use it
        clock.tick(fps)
        pygame.display.update()
        

if __name__ == "__main__":
    print('Author: ' + __author__)
    print('License: ' + __license__)
    print('Version: ' + __version__)
    print('Email: ' + __email__)
    print('Course: ' + __course__)
    print('Date: ' + __date__)
    print('Description: ' + __description__)
    print('# ' + '=' * 78)
    main()
