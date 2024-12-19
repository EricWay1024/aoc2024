lines = open("../input/19.in").read().split('\n')
lines = [l for l in lines if l != '']

patterns = lines[0].split(', ')
targets = lines[1:]
mem = dict()

def solve(target: str):
    if target == "":
        return True

    if mem.get(target) is not None:
        return mem[target]
    
    for p in patterns:
        if target.startswith(p) and solve(target[len(p):]):
            mem[target] = True
            return True
    
    mem[target] = False
    return False


ans = 0
for t in targets:
    if solve(t):
        ans += 1
print(ans)


            