'''
나의 접근법
    초를 증가시킬 때 마다 시/분/초를 구하고, 자리수를 구분한 다음, 자리수에 3이 포함되어 있는지 없는지를 따지는 코드다
책의 또 다른 접근법
    3중 for문을 시, 분, 초별로 돌면서 시, 분, 초를 문자열로 바꾼뒤, 'in'을 이용해 '3'이 하나라도 있는지 검사한다.
'''

import sys

N = int(sys.stdin.readline())

total_s = 0
h, m, s = 0, 0, 0
counter = 0

def sep(n):
    n_1 = n % 10
    n_10 = (n - n_1) // 10
    return [n_1, n_10]

while not(h == N and m == 59 and s == 59):
    s = total_s % 60
    m = (total_s // 60) % 60
    h = (total_s // 60) // 60
    
    sep_s = sep(s)
    sep_m = sep(m)
    sep_h = sep(h)

    if (sep_s[0] == 3 or sep_s[1] == 3 or sep_m[0] == 3 or sep_m[1] == 3 \
        or sep_h[0] == 3 or sep_h[1] == 3):
        counter += 1
    
    total_s += 1

print(counter)

# another solution
counter_2 = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                counter_2 += 1

print(counter)