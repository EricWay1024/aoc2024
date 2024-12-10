from queue import Queue
f = open("../input/10.in", "r").read().strip().split("\n")
f = [list(map(int, l)) for l in f]

n = len(f)
m = len(f[0])

vis = [[0 for _ in range(m)] for i in range(n)]

dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def bfs(x, y):
    q = Queue()

    q.put((x, y))

    vis[x][y] = 1

    ans = 0

    while not q.empty():
        a, b = q.get_nowait()

        if f[a][b] == 9:
            ans += 1
            continue

        for dx, dy in dirs:
            c, d = a + dx, b + dy

            if not (0 <= c < n and 0 <= d < m):
                continue

            if f[c][d] != f[a][b] + 1:
                continue

            vis[c][d] = 1
            q.put((c, d))
    
    return ans


res = 0
for a in range(n):
    for b in range(m):
        if f[a][b] == 0:
            vis = [[0 for _ in range(m)] for i in range(n)]
            res += bfs(a, b)


print(res)