""" 
나의 approach
    bisect 라이브러리를 사용하면 바로 찾을 수 있다.
 """

from bisect import bisect_left, bisect_right

N, X = map(int, input().split())

get_list = list(map(int, input().split()))

result = bisect_right(get_list, X) - bisect_left(get_list, X)
if result <= 0:
    print(-1)
else:
    print(result)