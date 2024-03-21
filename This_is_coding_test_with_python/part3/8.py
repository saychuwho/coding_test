""" 
나의 approach
    문자열을 받은 뒤에, 숫자는 더하고, 알파벳은 리스트에 append 한 뒤에 정렬했다.
 """

alpha = []
num = 0

S = input()

for s in S:
    if ord(s) > 47 and ord(s) < 58:
        num += int(s)
    else:
        alpha.append(s)

alpha = sorted(alpha)

for a in alpha:
    print(a, end="")

print(num)