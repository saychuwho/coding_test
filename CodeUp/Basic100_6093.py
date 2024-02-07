# Python Basic 100 - 6093

n = int(input())
seq = list(map(int, input().split()))

for num in reversed(seq):
    print(num, end=' ')