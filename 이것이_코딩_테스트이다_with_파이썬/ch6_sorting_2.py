""" 
나의 approach
    입력 규모가 작아서 그냥 내부 정렬을 써도 상관 없을거 같아서 내부 정렬을 이용했다
    
"""

import sys

N = int(sys.stdin.readline())

array = []
for _ in range(N):
    array.append(int(sys.stdin.readline()))

array.sort(reverse=True)

for num in array:
    print(num, end=' ')