f = open('../input/7.in').readlines()

def calculate(j, givens, res):
    n = len(givens)
    ans = givens[0]
    for i in range(1, n):
        op = [
            (lambda a, b: (a + b)) ,
            (lambda a, b: (a * b)),
            (lambda a, b: int(str(a) + str(b))),
        ][j % 3]
        ans = op(ans, givens[i])
        j //= 3
        if ans > res:
            return False
    return ans == res

def solve(res, givens):
    n = len(givens)
    for j in range(3 ** (n - 1)):
        if calculate(j, givens, res):
            return True
    return False

ans = 0
for i, line in enumerate(f): 
    nums = line.split(' ')
    res = int(nums[0].rstrip(':'))
    givens = list(map(int, nums[1:]))
    if solve(res, givens):
        ans += res

print(ans)