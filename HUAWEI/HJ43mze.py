def bfs(maze, start, points):
    W = lambda x, y: (x - 1, y)
    S = lambda x, y: (x + 1, y)
    A = lambda x, y: (x, y - 1)
    D = lambda x, y: (x, y + 1)
    child = []
    visited = list(points)
    end = (len(maze) - 1, len(maze[0]) - 1)
    for Move in [W, A, S, D]:
        t = (Move(start[0], start[1]))
        if not (0 <= t[0] < len(maze) and 0 <= t[1] < len(maze[0])):
            continue
        if not maze[t[0]][t[1]] and (t not in visited):
            if t == end:
                points.append(t)
                for p in points:
                    print("(%d,%d)" % (p[0], p[1]))
            else:
                child.append(t)
    if not child:
        return
    for t in child:
        points_new = points.copy()
        points_new.append(t)
        bfs(maze, t, points_new)


while True:
    try:
        maze = []
        [N, M] = list(map(int, input().split(" ")))
        for i in range(N):
            maze.append(list(map(int, input().strip().split(" "))))
        points = [(0, 0)]
        bfs(maze, (0, 0), points)
    except:
        break