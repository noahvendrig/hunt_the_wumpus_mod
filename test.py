import pygame
from sys import exit
import numpy
import random
from pygame.locals import *


def getChildren(graph, nodesAtLevel, hazardLocation, currLevel):
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
        hazardLocation not in visited
    ):  # check that the hazard' location isn't in the set of nodes that were just added to visited
        # print("\n")
        return getChildren(
            graph, visited, hazardLocation, currLevel
        )  # call the function again to recursively search through each layer

    else:
        return currLevel


def findHazard(graph):

    playerLocation = "n1"
    hazardLocation = "n12"
    currLevel = 0
    distance = 0

    if playerLocation != hazardLocation:
        distance = getChildren(graph, [playerLocation], hazardLocation, currLevel)
    else:
        distance = 0

    print("Hazard found %s nodes away from player" % distance)


def changeNode(graph, currNode, direction):  # direction: 0 = left, 1 = middle, 2=right
    index = random.randint(0, 2)
    print("index", index)
    nextNode = graph[currNode][index]
    print("moving from %s to %s" % (currNode, nextNode))

    return nextNode


def main():
    # findHazard(graph)
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
    w = 800
    h = 800
    bgColour = (255, 255, 255)
    running = True

    pygame.display.set_caption("Hunt the Wumpus")
    screen = pygame.display.set_mode((w, h))

    currNode = "n1"
    while running:
        for event in pygame.event.get():
            # if event.type == pygame.QUIT:
            #     running = False
            #     pygame.quit()
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

        screen.fill(bgColour)
        pygame.display.flip()


main()
