# Python Basic 100 - 6092

l = [0] * 23

n = int(input())
seq = list(map(int, input().split()))

for num in seq:
    l[num-1] += 1

for num in l:
    print(num, end=' ')