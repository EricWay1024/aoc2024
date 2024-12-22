with open('../input/22.in') as f:
    initial_secrets = [int(line.strip()) for line in f if line.strip()]
def get_2000th_secret(initial):
    s = initial
    for _ in range(2000):
        s = (s * 64) ^ s
        s %= 16777216
        s = s ^ (s // 32)
        s %= 16777216
        s = (s * 2048) ^ s
        s %= 16777216
    return s
total = sum(get_2000th_secret(s) for s in initial_secrets)
print(total)
