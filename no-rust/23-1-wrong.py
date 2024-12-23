# I misread the problem
# I thought connectivity was comopsable 

from collections import defaultdict
# lines = open("../input/23.in").read().strip().split('\n')
lines = open("test").read().strip().split('\n')

g = defaultdict(list)
ver = set()

for line in lines:
    a, b = line.split('-')
    g[a].append(b)
    g[b].append(a)
    ver.add(a)
    ver.add(b)


vis = defaultdict(bool)
def dfs(u):
    if vis[u]:
        return 0, 0
    vis[u] = True
    s1 = 1
    s2 = 1 if 't' not in u else 0
    for v in g[u]:
        r1, r2 = dfs(v)
        s1 += r1
        s2 += r2
    return s1, s2


def C3(n):
    return n * (n - 1) * (n - 2) // 6

ans = 0
for u in ver:
    s1, s2 = dfs(u)
    ans += C3(s1) - C3(s2)

print(ans)
