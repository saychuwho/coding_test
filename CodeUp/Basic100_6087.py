# Python Basic 100 - 6087

num = int(input())

for i in range(1, num+1):
    if i % 3 == 0:
        continue
    print(i, end=' ')