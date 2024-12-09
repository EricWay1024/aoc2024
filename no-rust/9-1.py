f = open("../input/9.in", "r").read().strip()

# f = '2333133121414131402'
total = 0

m = []
id_num = 0

for i, c in enumerate(f):
    k = int(c)

    for _ in range(k):
        if (i % 2) == 1:
            m.append(-1)
        else:
            m.append(id_num)

    if (i % 2) == 1:
        id_num += 1

i, j = 0, len(m) - 1

while True:
    while m[i] != -1:
        i += 1
    while m[j] == -1:
        j -= 1
    
    if i >= j:
        break

    m[i], m[j] = m[j], m[i]

# print(m)
ans = 0
for i, k in enumerate(m):
    if k == -1:
        break
    ans += i * k
print(ans)