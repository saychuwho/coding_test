'''
내 코드 approach : 
    n이 어차피 크기가 1000 이하니까, 내장 sort 함수를 사용해도 된다. 
    그러면 array를 정렬한 뒤 제일 뒤 수랑 그 앞에 있는 수만 필요하다.
'''

import sys

n, m, k = map(int, sys.stdin.readline().split())

array = list(map(int, sys.stdin.readline().split()))

array.sort()

sum = 0
counter = 1
for _ in range(m):
    if counter % k == 0:
        sum += array[-2]
        counter = 1
    else:
        sum += array[-1]
        counter += 1

print(sum)

'''
다른 approach
    m이 굉장히 큰 수라면 이 방법은 시간초과가 난다.
    수열의 규칙을 이용해서 for문 없이 구할 수 있다.
    정렬된 array의 제일 뒤 수를 k번 더한 뒤에 그 앞의 수를 한 번 더하는 패턴이 반복된다.
    그러면 이 k+1 패턴이 몇번 반복되는지 파악하기만 하면 된다.
    k+1 패턴이 몇번 반복되는지 파악한 뒤에, 남은 횟수만큼 array 제일 뒤 수를 더하면 된다
'''

pattern_num = (m // (k+1))
rest_num = m % (k+1)
sum_2 = (k*array[-1] + array[-2])*pattern_num + rest_num*array[-1]
print(sum_2)