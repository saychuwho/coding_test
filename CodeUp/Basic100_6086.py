# Python Basic 100 - 6086

num = int(input())

sum = 0
i = 0
while True:
    i += 1
    sum += i
    if sum >= num:
        break

print(sum)