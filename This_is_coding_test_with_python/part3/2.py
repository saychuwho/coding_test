""" 
나의 approach
    0 빼고 다 곱하면 제일 큰 수가 나온다
 """

S = input()

result = 1
for s in S:
    if s == '0':
        continue
    result *= int(s)

print(result)