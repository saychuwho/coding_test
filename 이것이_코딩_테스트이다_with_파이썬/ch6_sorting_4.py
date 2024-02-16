""" 
나의 approach
    A와 B를 정렬한 다음에 A의 최솟값이 있는 부분과 B의 최댓값들이 있는 부분을 바꾸면 되는게 아닌가 라고 처음에 코드를 짬
    근데 B의 최댓값들이 A의 최솟값보다 작을수도 있다는 사실을 생각안함
    바꾼 코드 : A의 최솟값이 B의 최댓값보다 작을 때만 swap함.
또 다른 approach
    B를 내림차순으로 정렬하는거다. 그러면 array_b[-i-1] 같은 복잡한 연산을 안해도 된다.
"""

import sys

N, K = map(int, sys.stdin.readline().split())
array_a = list(map(int, sys.stdin.readline().split()))
array_b = list(map(int, sys.stdin.readline().split()))

array_a.sort()
array_b.sort()

# old_solution
# new_array = array_a[K:] + array_b[len(array_b)- K:]
# print(sum(new_array))

for i in range(K):
    if array_a[i] <= array_b[-i-1]:
        array_a[i], array_b[-i-1] = array_b[-i-1], array_a[i]

print(sum(array_a))