f = open("../input/9.in", "r").read().strip()

# f = '2333133121414131402'

def get_range(m, i):
    a, b = i, i
    while a >= 1 and m[a - 1] == m[i]:
        a -= 1
    while b + 1 < len(m) and m[b + 1] == m[i]:
        b += 1
    return a, b


# Failed attempt below
g = [[int(c), -1 if (i % 2) == 1 else i // 2] for i, c in enumerate(f)]

# print(g)
# # (x, 1) is file
# # (x, 0) is empty

# j = len(g) - 1


# attempted = set()
# while True:
#     while g[j][1] == -1 or g[j][0] in attempted:
#         j -= 1
#         if j < 0:
#             break
    
#     if j < 0:
#         break
    
#     attempted.add(g[j][0])
#     for i in range(j):
#         if g[i][1] != -1 or g[i][0] < g[j][0]:
#             continue
        
#         g[j][1] = -1

#         if g[i][0] == g[j][0]:
#             g[i][1] = g[j][1]
#         else:
#             diff = g[i][0] - g[j][0]
#             g[i][1] = g[j][1]
#             g[i][0] = g[j][0]

#             g.insert(i + 1, [diff, -1])
#             j += 1
    
#     print(j, g)
# print(g)


# Another method, but Python is too slow
# So it's rewritten in C++

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

j = len(m) - 1

while j >= 0:
    a, b = get_range(m, j)
    len_j = b - a + 1
    i = 0
    while i < j:
        if m[i] != -1:
            i += 1
            continue
        
        c, d = get_range(m, i)
        len_i = d - c + 1
        if len_i >= len_j:
            for k in range(0, len_j):
                m[c + k], m[a + k] = m[a + k], m[c + k]
            break
        else:
            i = d + 1
    j -= 1
    print(j) 



print(m)
ans = 0
for i, k in enumerate(m):
    if k == -1:
        continue
    ans += i * k
print(ans)