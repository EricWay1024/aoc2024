from queue import Queue
f = open("../input/10.in", "r").read().strip().split("\n")
f = [list(map(int, l)) for l in f]
n, m = len(f), len(f[0])
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def bfs(x, y):
    q = Queue()
    q.put((x, y))
    ans = 0
    while not q.empty():
        a, b = q.get()
        if f[a][b] == 9:
            ans += 1
            continue
        for dx, dy in dirs:
            c, d = a + dx, b + dy
            if 0 <= c < n and 0 <= d < m and f[c][d] == f[a][b] + 1:
                q.put((c, d))
    return ans

res = 0
for a in range(n):
    for b in range(m):
        if f[a][b] == 0:
            res += bfs(a, b)
print(res)