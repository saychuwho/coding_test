""" 
나의 approach
    1,000,000 개가 들어오면 counting sort랑 binary search를 써야 하나....
    100,000은 확실히 내장 sort를 사용해도 되는데
    counting sort를 사용하기에는 memory가 부족하다. 정수가 1,000,000만이니까. >> 아니다. counting sort 충분히 사용할 수 있었다. 4MB밖에 안먹으니까.
    일단은 그냥 sort를 사용하고, search만 binary search를 사용하자.
또 다른 approach
    1. counting sort를 이용할 수 있다.
    2. python의 set 자료형을 이용할 수 있다.
 """

import sys

N = int(sys.stdin.readline().rstrip())
parts = list(map(int, sys.stdin.readline().rstrip().split()))

M = int(sys.stdin.readline().rstrip())
requested_parts = list(map(int, sys.stdin.readline().rstrip().split()))

""" 1. binary search """
def binary_search(array, target, start, end):
    mid = (start + end) // 2
    if start > end:
        return False
    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)
    
parts_1 = sorted(parts)

for requested_part in requested_parts:
    if binary_search(parts_1, requested_part, 0, N-1):
        print("yes", end=' ')
    else:
        print("no", end=' ')

""" 2. counting sort """
print()

counting_array = [0] * 1000001

for part in parts:
    counting_array[part] += 1

for requested_part in requested_parts:
    if counting_array[requested_part] > 0:
        print("yes", end=' ')
    else:
        print("no", end=' ')

""" 3. `set` data structure """
print()

parts_set = set(parts)

for requested_part in requested_parts:
    if requested_part in parts_set:
        print("yes", end=' ')
    else:
        print("no", end=' ')