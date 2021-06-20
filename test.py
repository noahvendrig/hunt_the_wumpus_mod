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

# print("ee", graph["n6"])


playerLocation = ["n6"]
# playerLocation = ["n5", "n7", "n15"]
wumpusLocation = "n14"

currLevel = 0
visited = []


def getChildren(nodesAtLevel, visited):
    for node in nodesAtLevel:
        if node not in visited:
            visited.extend(graph[node])
            visited = list(set(visited))
            print(node, "   ", visited)
    return visited


if playerLocation != wumpusLocation:
    while wumpusLocation not in visited and currLevel < 5:
        currLevel += 1
        print("Level:", currLevel)
        r = getChildren(playerLocation, visited)

        if wumpusLocation in visited:
            print("WUMPUS FOUND !!")
# c = ["n6"]
# level = 1
# while wumpusLocation not in c:
#     level += 1
#     c = getChildren(c)
#     c = list(set(c))
#     print(c)

# print(level)
