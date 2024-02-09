# Python Basic 100 - 6083

r, g, b = map(int, input().split())

num = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            num += 1

print(num)