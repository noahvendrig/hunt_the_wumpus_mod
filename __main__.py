# Using a Python dictionary to act as an adjacency list
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

playerLocation = "n6"
wumpusLocation = "n19"



counter = 0
done = False

visited = []  # List to keep track of visited nodes.
queue = []  # Initialize a queue


def bfs(visited, graph, node, counter, done):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        if s == wumpusLocation:
            print("found wumpus at", s, "counter=", counter)
        else:
            print(s)  # , end=" ")

        for neighbour in graph[s]:

            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Driver Code
bfs(visited, graph, playerLocation, counter, done)
