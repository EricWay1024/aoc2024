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

all_points = [(i, j) for i in range(n) for j in range(m) if lines[i][j] != '#']
ans = 0


# rather slow, but acceptable
for (ax, ay) in all_points:
    for (bx, by) in all_points:
        steps = abs(ax - bx) + abs(ay - by)
        if steps > 20:
            continue
        time_saved = dis[bx][by] - dis[ax][ay] - steps
        if time_saved >= 100:
            ans += 1

print(ans)
