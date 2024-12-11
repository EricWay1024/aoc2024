f = open("../input/11.in", "r").read().strip().split(" ")
f = [int(x) for x in f]

def blink(f):
    nf = []
    for x in f:
        if x == 0:
            nf.append(1)
        elif (len(str(x)) % 2) == 0:
            s = str(x)
            n = len(s)
            nf.append(int(s[:n // 2]))
            nf.append(int(s[(n//2):]))
        else:
            nf.append(x * 2024)
    return nf

for i in range(75):
    f = blink(f)
    print(i, len(f))

print(len(f))