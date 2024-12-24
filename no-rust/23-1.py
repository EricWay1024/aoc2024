from collections import defaultdict
lines = open("../input/23.in").read().strip().split('\n')

g = defaultdict(bool)
ver = set()

for line in lines:
    a, b = line.split('-')
    g[(a, b)] = True
    g[(b, a)] = True
    ver.add(a)
    ver.add(b)


ans = 0

def valid(s: str):
    return s.startswith('t')

for a in ver:
    for b in ver:
        for c in ver:
            if g[(a, b)] and g[(b, c)] and g[(a, c)] and (valid(a) or valid(b) or valid(c)):
                ans += 1

print(ans // 6)