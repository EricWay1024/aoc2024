from collections import defaultdict
lines = open("../input/23.in").read().strip().split('\n')
# lines = open("test").read().strip().split('\n')

g = defaultdict(bool)
h = defaultdict(list)
ver = set()

for line in lines:
    a, b = line.split('-')
    g[(a, b)] = True
    g[(b, a)] = True
    h[a].append(b)
    h[b].append(a)
    ver.add(a)
    ver.add(b)


threes = set()

ver = list(ver)
ver_num = len(ver)
for i in range(ver_num):
    a = ver[i]
    for j in range(i):
        b = ver[j]
        if not g[(a, b)]: continue
        for k in range(j):
            c = ver[k]
            if g[(b, c)] and g[(a, c)]:
                threes.add(tuple(sorted([a, b, c])))

ns = [set() for _ in range(1000)]

ns[3] = threes
for i in range(4, 100):
    for v in ver:
        for s in ns[i - 1]:
            if all(g[(u, v)] for u in s):
                ns[i].add(tuple(sorted(list(s) + [v])))
    print('Calculating i =', i, len(ns[i]))
    if len(ns[i]) == 0:
        for s in ns[i - 1]:
            print(','.join(sorted(list(s))))
        break
