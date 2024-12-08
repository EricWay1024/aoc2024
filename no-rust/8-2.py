from collections import defaultdict
f = open("../input/8.in", "r").read().strip().split("\n")
m = len(f[0])
n = len(f)
mem = defaultdict(list)

for i in range(n):
    for j in range(m):
        if f[i][j] == '.':
            continue
        mem[f[i][j]].append((i, j))

ans = set()
for lst in mem.values():
    for (i, j) in lst:
        for (k, l) in lst:
            if i == k and j == l: 
                continue
            dx = k - i
            dy = l - j
            x, y = i, j
            while 0 <= x < n and 0 <= y < m:
                ans.add((x, y))
                x += dx
                y += dy

print(len(ans))