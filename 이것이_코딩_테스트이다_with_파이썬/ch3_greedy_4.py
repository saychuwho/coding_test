'''
나의 approach
    계속 나누다가, 나눌 수 없으면 1을 빼는 식으로 코드를 작성함
다른 생각
    n이 100억 같은 매우 큰 수라면? 
    나머지를 한꺼번에 빼서 빼는 횟수를 좀 줄일 수 있다.
'''

import sys

n, k = map(int, sys.stdin.readline().split())

counter = 0
n_temp = n
while n != 1:
    if n % k == 0:
        n /= k
    else:
        n -= 1
    
    counter += 1

# another solution
counter_2 = 0
while n_temp != 1:
    if n_temp % k != 0:
        counter_2 += (n_temp % k)
        n_temp -= (n_temp % k)
    else:
        n_temp /= k
        counter_2 += 1

print(counter)
print(counter_2)