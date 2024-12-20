lines = open("../input/20.in").read().strip().split('\n')
n, m = len(lines), len(lines[0])
INF = -1
dis = [[INF for _ in range(m)] for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

sx, sy, ex, ey = None, None, None, None
for i in range(n):
    for j in range(m):
        if lines[i][j] == 'S':
            sx, sy = i, j 
        elif lines[i][j] == 'E':
            ex, ey = i, j

x, y = sx, sy
dis[x][y] = 0

while True:
    for (dx, dy) in dirs:
        nx, ny = x + dx, y + dy
        if lines[nx][ny] != '#' and dis[nx][ny] == INF:
            dis[nx][ny] = dis[x][y] + 1
            x, y = nx, ny
            break
    
    if (x, y) == (ex, ey):
        break
from pprint import pprint
pprint(dis)

all_points = [(i, j) for i in range(n) for j in range(m)]
ans = 0

for (ax, ay) in all_points:
    if lines[ax][ay] == '#':
        continue
    for (dx1, dy1) in dirs:
        bx, by = ax + dx1, ay + dy1
        if lines[bx][by] != '#':
            continue
        for (dx2, dy2) in dirs:
            cx, cy = bx + dx2, by + dy2
            try:
                if lines[cx][cy] == '#':
                    continue
            except IndexError:
                continue

            time_saved = dis[cx][cy] - dis[ax][ay] - 2
            if time_saved >= 100:
                ans += 1


print(ans)
