
# I believe this algorithm is right 
# but I always encounter RecursionError: maximum recursion depth exceeded
# when running it
f = open("../input/11.in", "r").read().strip().split(" ")

f = [int(x) for x in f]
mem = dict()

def dp(x, n):
    if n == 0:
        return 1
    
    if mem.get((x, n)) is not None:
        return mem[(x, n)]
    
    if x == 0:
        mem[(x, n)] = dp(1, n - 1)
    elif (len(str(x)) % 2) == 0:
        s = str(x)
        n = len(s)
        a = int(s[:n // 2])
        b = int(s[(n//2):])
        mem[(x, n)] = dp(a, n - 1) + dp(b, n - 1)
    else:
        mem[(x, n)] = dp(x * 2024, n - 1)
    
    return mem[(x, n)]


print(sum(dp(x, 75) for x in f))