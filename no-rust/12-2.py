from collections import defaultdict
f = open("../input/12.in", "r").read().strip().split("\n")
n, m = len(f), len(f[0])
vis = [[0 for _ in range(m)] for _ in range(n)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def count_side(sides):
    ans = 0
    for lst in sides.values():
        lst.sort()
        while lst:
            ans += 1
            c = lst[-1]; lst.pop()
            while lst and lst[-1] == c - 1:
                c = lst[-1]; lst.pop()
    return ans


def dfs(x, y):
    if vis[x][y] == 1:
        return 0
    a = 1
    vis[x][y] = 1
    for i, (dx, dy) in enumerate(dirs):
        xc, yc = x + dx, y + dy
        if (not (0 <= xc < n and 0 <= yc < m)) or f[xc][yc] != f[x][y]:
            if i in [0, 1]:
                four_sides[i][y].append(x)
            else:
                four_sides[i][x].append(y)
            continue
        ac = dfs(xc, yc)
        a += ac
    return a

total = 0
for i in range(n):
    for j in range(m):
        four_sides = [defaultdict(list) for _ in range(4)]
        a = dfs(i, j)
        p = sum(count_side(sides) for sides in four_sides)
        total += a * p

print(total)