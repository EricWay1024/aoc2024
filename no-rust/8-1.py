from collections import defaultdict
f = open('../input/8.in').readlines()

f = [line.rstrip('\n') for line in f]

print(f)

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
            
            x, y = 2 * k - i, 2 * l - j

            if 0 <= x < n and 0 <= y < m:
                ans.add((x, y))


print(len(ans))