""" 
나의 approach
    일단 정렬을 한다. 길이기 10억이면 counting sort를 못 사용하니, 그냥 sort를 사용한다
    정렬을 한 뒤에 제일 큰 거를 기준으로 1씩 줄여나가면서 N을 맞출 수 있지 않을까? 이건 너무 크다
    아니면 정렬을 사용하지 말고, 길이 자체를 binary search 기법으로 찾는거다. max 구한 뒤에. 잘라가면서 찾는거다.
또 다른 approach
    iterative로 구해볼 수 있다.
 """

import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))

""" original solution : recurrsive """

start = 0
end = max(array)

def binary_search(array, target, start, end):
    mid = (start + end) // 2

    # 자른 sum 구하기
    sum_result = 0
    for length in array:
        sum_result += length - mid if length - mid > 0 else 0
    
    # binary search
    if target == sum_result:
        return mid
    elif target > sum_result:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)
    
print(binary_search(array, M, start, end))

""" another solution : iterative """

res = 0
start = 0
end = max(array)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)