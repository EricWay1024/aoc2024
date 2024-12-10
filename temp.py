ans = 0
for a in [1,2,3]:
    for b in [1,2,3]:
        for c in [1,2,3]:
            for d in [1,2,3]:
                if 10 < a * b * c * d < 20:
                    ans += 1


print(ans)

for i in range(30, 70):
    print(i, (i+1) * i // 2)