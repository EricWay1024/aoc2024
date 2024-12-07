f = open('../input/7.in').readlines()


def calculate(j, givens):
    n = len(givens)
    ans = givens[0]
    for i in range(1, n):
        op = (lambda a, b: (a + b)) if ((j & 1) == 1) else (lambda a, b: (a * b))
        ans = op(ans, givens[i])
        j >>= 1
    return ans

def solve(res, givens):
    n = len(givens)

    for j in range(1 << (n - 1)):
        if calculate(j, givens) == res:
            return True
    
    return False

ans = 0
for line in f: 
    nums = line.split(' ')
    res = int(nums[0].rstrip(':'))
    givens = list(map(int, nums[1:]))
    if solve(res, givens):
        ans += res

print(ans)