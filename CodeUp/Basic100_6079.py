# Python Basic 100 - 6079

sum = 0
num = int(input())

i = 1
while True:
    sum += i
    if sum >= num:
        break
    i += 1

print(i)
