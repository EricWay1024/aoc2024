from functools import lru_cache
lines = [l for l in open("../input/19.in").read().split('\n') if l != '']
patterns = lines[0].split(', ')
targets = lines[1:]
@lru_cache(maxsize=None)
def solve(target: str):
    return 1 if target == "" else sum(
        solve(target[len(p):]) for p in patterns if target.startswith(p))

print(sum(solve(t) for t in targets))