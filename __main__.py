import pygame  # after activating conda env run the following in cmd: 'pip install pygame'
from sys import exit
import numpy
import random
from pygame.locals import *
import re


class hazard:
    def __init__(self):
        self.type = "hazard"
        self.pos = getRandomNode()
        self.alertDistance = 1


class wumpus(hazard):
    def __init__(self):
        hazard.__init__(self)


class pit(hazard):
    def __init__(self):
        hazard.__init__(self)


class bat(hazard):
    def __init__(self):
        hazard.__init__(self)


class player:
    def __init__(self):
        self.type = "player"
        self.pos = getRandomNode()

    def detectHazardCollision(self, playerPos, wumpusPos, pitNodes, batNodes):
        if playerPos in [wumpusPos]:
            return "wumpus"

        if playerPos in pitNodes:
            return "pit"

        if playerPos in batNodes:
            return "bat"
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


def findHazard(graph, playerPos, hazardPos):

    currLevel = 0
    distance = 0

    if playerPos != hazardPos:
        distance = getChildren(graph, [playerPos], hazardPos, currLevel)
    else:
        distance = 0

    # print("Hazard found %s nodes away from player" % distance)
    return distance


def changeNode(graph, currNode, direction):  # direction: 0 = left, 1 = middle, 2=right
    nextNode = graph[currNode][direction]
    print("moving from %s to %s" % (currNode, nextNode))
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

    w = 1000
    h = 800

    bgColour = (255, 255, 255)
    running = True

    pygame.display.set_caption("Hunt the Wumpus")
    screen = pygame.display.set_mode((w, h))
    fontColour = (0, 0, 0)

    # font = ("./arial.tff", 32)
    font = pygame.font.Font("freesansbold.ttf", 32)

    # currNode = "n1"  # set the starting node
    # settings: ##########################################################
    batsNum = 2
    pitNum = 2
    wumpusNum = 1
    playerInstance = player()
    wumpusInstance = wumpus()
    currNode = playerInstance.pos

    batNodes = []
    pitNodes = []
    wumpusNodes = []

    # for w in range(wumpusNum):
    #     wumpusInstance = wumpus()
    #     wumpusNodes.append(wumpusInstance.pos)

    for b in range(batsNum):
        batInstance = bat()
        batNodes.append(batInstance.pos)

    for p in range(pitNum):
        pitInstance = pit()
        pitNodes.append(pitInstance.pos)

    ################################################
    bgImg = pygame.image.load("./img/bg.jpg")
    bgImg = pygame.transform.scale(bgImg, (w, h))

    while running:
        playerInstance.detectHazardCollision(
            currNode,
            wumpusInstance.pos,
            pitInstance.pos,
            batInstance.pos,
        )
        # note only update wumpus pos when the player's position is updated - not every iteration in the while loop. call findhazard from changenode and then return wumpusPos. pass back to main function then pass to showText()
        screen.fill(bgColour)  # fill before anything else
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # close when x button hit
                running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()

                if event.key == pygame.K_LEFT:
                    currNode = changeNode(graph, currNode, 0)
                if event.key == pygame.K_UP:
                    currNode = changeNode(graph, currNode, 1)
                if event.key == pygame.K_RIGHT:
                    currNode = changeNode(graph, currNode, 2)

        screen.blit(bgImg, (1, 1))
        # wumpusDistance = findHazard(graph, currNode, wumpusInstance.pos)
        wumpusDistance = findHazard(graph, currNode, wumpusInstance.pos)
        showText(currNode, w, h, fontColour, font, screen, graph, wumpusDistance)
        pygame.display.update()


main()
