
cave = {
        1: [2, 5, 8],
        2: [10, 3, 1],
        3: [2, 4, 12],
        4: [3, 5, 14],
        5: [1, 4, 6],
        6: [5, 7, 15],
        7: [6, 8, 17],
        8: [1, 7, 9],
        9: [8, 10, 18],
        10: [11, 9, 2],
        11: [10, 12, 19],
        12: [3, 11, 13],
        13: [12, 14, 20],
        14: [4, 13, 20],
        15: [6, 14, 16],
        16: [15, 17, 20],
        17: [7, 16, 18],
        18: [9, 17, 19],
        19: [11, 18, 20],
        20: [13, 16, 19],
    }

# bfs = breadth_first_search(player_pos, target, cave)
print("↑↓")

def findPlayer(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)


playerpos = 9
wumpuspos = 13
# RETURNS THE PATH BETWEEN WUMPUS AND PLAYER
path = findPlayer(cave, playerpos, wumpuspos)

# update the wumpus' position to the next node in the path. we use index one since the path is a list and the next node is the second index.
wumpuspos = path[1]

print(path)
# print(bfs)
