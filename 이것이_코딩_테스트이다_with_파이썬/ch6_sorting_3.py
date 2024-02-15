""" 
나의 approach
    입력이 100,000 이하면, 내장 정렬이 O(NlogN)에 수행되니까 사용해도 될 거 같아서 사용함
또 다른 approach
    이거를 counting sort를 이용해 풀 수 있을까? 이름 순서대로 나와야 하는데....
    array에 튜플 그대로 넣으면 될 거 같다. 성적이 동일한 학생들의 순서는 자유롭게 출력해도 된다고 하니까...
"""

import sys

N = int(sys.stdin.readline())

array = []
for _ in range(N):
    name, score = sys.stdin.readline().split()
    array.append((name, int(score)))

# using python internal sorted()
array_2 = sorted(array, key=lambda x : x[1])

for name, score in array_2:
    print(name, end=' ')

# using counting sort
print()

array_3 = [[] for _ in range(101)]
for name, score in array:
    array_3[score].append(name)

for names in array_3:
    for name in names:
        print(name, end=' ')