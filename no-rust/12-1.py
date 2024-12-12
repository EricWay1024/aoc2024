f = open("../input/12.in", "r").read().strip().split("\n")
n, m = len(f), len(f[0])

vis = [[0 for i in range(m)] for j in range(n)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x, y):
    if vis[x][y] == 1:
        return 0, 0

    a = 1
    p = 0
    vis[x][y] = 1
    for dx, dy in dirs:
        xc, yc = x + dx, y + dy
        if not (0 <= xc < n and 0 <= yc < m):
            p += 1
            continue
        if f[xc][yc] != f[x][y]:
            p += 1
        else:
            ac, pc = dfs(xc, yc)
            a += ac
            p += pc
    return a, p


total = 0
for i in range(n):
    for j in range(m):
        a, p = dfs(i, j)
        total += a * p

print(total)