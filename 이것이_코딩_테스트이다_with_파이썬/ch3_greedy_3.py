'''
나의 approach
    각 행 별로 제일 작은 수를 뽑아낸 다음, 뽑아낸 수들 중 제일 큰수를 출력하면 된다.
    n, m 모두 적은 수이니 기본 함수를 사용해도 된다.
    처음에는 .sort()를 사용했지만, min(), max()만 뽑아내면 되니 그걸 사용하는 방법으로 코드를 바꿨다

교재 solution을 보고 난 뒤 첨언
    container에 값을 넣는 대신에, 기존에 제일 큰 값과 새로 찾은 행의 가장 작은 값들만 비교하면 된다.
    더 나은 approach를 주석 표시한 곳에 넣어뒀다.
'''

import sys

n, m = map(int, sys.stdin.readline().split())

container = []
result = 0 # better solution
for _ in range(n):
    tmp_list = list(map(int, sys.stdin.readline().split()))
    container.append(min(tmp_list))
    result = max(result, min(tmp_list)) # better solution

print(max(container))
print(result) # better solution