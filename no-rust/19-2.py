lines = open("../input/19.in").read().split('\n')
lines = [l for l in lines if l != '']

patterns = lines[0].split(', ')
targets = lines[1:]
mem = dict()

def solve(target: str):
    if target == "":
        return 1

    if mem.get(target) is not None:
        return mem[target]
    
    res = 0
    for p in patterns:
        if target.startswith(p):
            res += solve(target[len(p):])
            
    mem[target] = res
    return res


ans = 0
for t in targets:
    ans += solve(t)
print(ans)


            