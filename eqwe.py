
cave = {1: [2, 3, 4], 2: [1, 5, 6], 3: [1, 7, 8], 4: [1, 9, 10], 5: [2, 9, 11],
        6: [2, 7, 12], 7: [3, 6, 13], 8: [3, 10, 14], 9: [4, 5, 15], 10: [4, 8, 16],
        11: [5, 12, 17], 12: [6, 11, 18], 13: [7, 14, 18], 14: [8, 13, 19],
        15: [9, 16, 17], 16: [10, 15, 19], 17: [11, 20, 15], 18: [12, 13, 20],
        19: [14, 16, 20], 20: [17, 18, 19]}

# bfs = breadth_first_search(player_pos, target, cave)


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


playerpos = 3
wumpuspos = 10
# RETURNS THE PATH BETWEEN WUMPUS AND PLAYER
path = findPlayer(cave, playerpos, wumpuspos)

# update the wumpus' position to the next node in the path. we use index one since the path is a list and the next node is the second index.
wumpuspos = path[1]

print(path)
# print(bfs)
