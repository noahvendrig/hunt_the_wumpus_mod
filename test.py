import pygame
import sys
import numpy
import random


def getChildren(graph, nodesAtLevel, wumpusLocation, currLevel):
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
        wumpusLocation not in visited
    ):  # check that the wumpus' location isn't in the set of nodes that were just added to visited
        # print("\n")
        return getChildren(
            graph, visited, wumpusLocation, currLevel
        )  # call the function again to recursively search through each layer

    else:
        print("Wumpus found %s nodes away from player" % currLevel)
        return currLevel


def findDistance():

    graph = {
        "n1": ["n2", "n5", "n8"],
        "n2": ["n1", "n3", "n10"],
        "n3": ["n2", "n4", "n12"],
        "n4": ["n3", "n5", "n14"],
        "n5": ["n1", "n4", "n6"],
        "n6": ["n5", "n7", "n15"],
        "n7": ["n6", "n8", "n17"],
        "n8": ["n1", "n7", "n9"],
        "n9": ["n8", "n10", "n18"],
        "n10": ["n2", "n9", "n11"],
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

    playerLocation = "n1"
    wumpusLocation = "n12"
    currLevel = 0
    distance = 0

    if playerLocation != wumpusLocation:
        distance = getChildren(
            graph, [playerLocation], wumpusLocation, currLevel)
    else:
        distance = 0

    return distance
    # print("distance:", distance)


def main():

    pygame.init()
    w = 800
    h = 800
    bgColour = (255, 255, 255)
    running = True

    pygame.display.set_caption('Hunt the Wumpus')
    screen = pygame.display.set_mode((w, h))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        screen.fill(bgColour)
        pygame.display.flip()

        for num in range(findDistance()):
            pygame.draw.circle(screen, (0, 0, 255),
                               (250, 250), random.randint(0, 100))


main()
