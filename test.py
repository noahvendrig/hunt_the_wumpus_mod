import pygame  # after activating conda env run the following in cmd: 'pip install pygame'
from sys import exit, float_repr_style
import numpy
import random
from pygame.locals import *
import re
import time

s = time.time()
print(s)


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


def validInputReceived(
    graph, currNode, keyNum, wumpusInstance, pits, bats, playerInstance
):
    wumpusPos = wumpusInstance.pos

    currNode = changeNode(graph, currNode, keyNum)
    wumpusDist = findHazard(graph, currNode, wumpusPos)
    return currNode, wumpusDist


def findHazard(graph, playerPos, hazardPos):

    currLevel = 0
    distance = 0

    if playerPos != hazardPos:
        distance = getChildren(graph, [playerPos], hazardPos, currLevel)
    else:
        distance = 0

    print(f"Hazard found {distance} nodes away from player at {playerPos}")
    return distance


def changeNode(graph, currNode, direction):  # direction: 0 = left, 1 = middle, 2=right
    nextNode = graph[currNode][direction]
    # print("moving from %s to %s" % (currNode, nextNode))
    return nextNode


def showText(currNode, w, h, fontColour, font, screen, graph, wumpusDistance):
    roomL_X = (w * 0.1) - 100
    roomL_Y = h / 2
    roomM_X = (w / 2) - 50
    roomM_Y = h * 0.1
    roomR_X = (w * 0.9) - 25
    roomR_Y = h / 2

    currRoom_X = (w / 2) - 50
    currRoom_Y = h / 2

    # DISTANCE

    distanceTxt = font.render(
        "Wumpus is %s nodes away" % wumpusDistance,
        True,
        fontColour,  # finds integers in the string e.g. "19" in "n19" to display
    )
    screen.blit(distanceTxt, (500, 700))  # draw on screen
    ##

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


def wumpusDeath():
    pass


def pitDeath():
    pass


def hazardEffect(colObj):
    newPlayerPos = ""
    if colObj.type == "wumpus":
        print(f"just hit the WUMPUS at {colObj.pos}")
        # wumpusDeath()

    elif colObj.type == "pit":
        print(f"just hit a PIT at {colObj.pos}")
        # pitDeath()

    elif colObj.type == "bat":
        print(f"just hit a BAT at {colObj.pos}")
        newPlayerPos = getRandomNode()
        return newPlayerPos
    return


def showBat(screen, batImg):
    screen.blit(batImg, (400, 100))
    pygame.display.update()


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
    # arialFont = pygame.font.SysFont("Arial", 30)
    frameCount = 0

    w = 1600
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
    wumpusNum = 1
    playerInstance = player()
    wumpusInstance = wumpus()

    # currNode = playerInstance.pos
    currNode = "n1"
    print(f"initial {currNode = }")
    bats = []
    pits = []

    wumpusNodes = []

    # for w in range(wumpusNum):
    #     wumpusInstance = wumpus()
    #     wumpusNodes.append(wumpusInstance.pos)
    batNodes = []  #################################### delete later
    pitNodes = []  #################################### delete later
    for b in range(batsNum):
        batInstance = bat()
        if batInstance.pos == playerInstance.pos or batInstance.pos != "n2":
            batInstance.pos = "n2"  # getRandomNode()
        bats.append(batInstance)
        batNodes.append(batInstance.pos)

    for p in range(pitNum):
        pitInstance = pit()
        if pitInstance.pos == playerInstance.pos:
            pitInstance.pos = getRandomNode()
        pits.append(pitInstance)
        pitNodes.append(pitInstance.pos)

    print(f"{wumpusInstance.pos = }")

    print(f"{pitNodes = }")  #################################### delete later
    print(f"{batNodes = }")  #################################### delete later

    ################################################
    bgImg = pygame.image.load("./img/bg.jpg")
    bgImg = pygame.transform.scale(bgImg, (w, h))

    batImg = pygame.image.load("./img/bats.png")
    batImg = pygame.transform.scale(batImg, (500, 500))

    clock = pygame.time.Clock()

    wumpusDistance = findHazard(
        graph, currNode, wumpusInstance.pos
    )  # calculate initial wumpus distance from spawn
    colObj = playerInstance.detectHazardCollision(currNode, wumpusInstance, pits, bats)
    if colObj != "null":
        raise Exception(f"collided object = {colObj}")

    while running:
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
                    currNode, wumpusDistance = validInputReceived(
                        graph,
                        currNode,
                        0,
                        wumpusInstance,
                        pits,
                        bats,
                        playerInstance,
                    )

                if event.key == pygame.K_UP:
                    currNode, wumpusDistance = validInputReceived(
                        graph,
                        currNode,
                        1,
                        wumpusInstance,
                        pits,
                        bats,
                        playerInstance,
                    )

                if event.key == pygame.K_RIGHT:
                    currNode, wumpusDistance = validInputReceived(
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
                    effect = hazardEffect(colObj)
                    if effect is not None:
                        currNode = effect

                        print("show bats!")
                        startFrames = frameCount
                        duration = 5 * fps
                        currFrames = 0

                        while startFrames + duration > currFrames:

                            # print(f"{startFrames, duration, currFrames}")

                            currFrames += 25
                            # clock.tick(0.1)
                            # time.sleep(4)

                        while True:
                            showBat(screen, batImg)
        # screen.blit(batImg, (1, 1))
        showText(currNode, w, h, fontColour, font, screen, graph, wumpusDistance)
        pygame.display.update()
        frameCount += fps
        print(frameCount, end=" ")
        clock.tick(fps)


main()
