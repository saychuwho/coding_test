""" 
나의 approach
    DP를 별개로 두고, 예전에 이거 비슷한 문제를 BFS로 풀었던 기억이 난다.
    일단 BFS로 한 번 풀어보고, DP 풀이를 생각해보자: 쉽게 생각이 안난다...
책의 approach
    문제에서 요구하는 것을 점화식으로 구성할려고 생각해보면 고민하면 그 다음 DP로 코딩은 쉽다
    이 문제에서는 수 i에서 "연산을 처리한 뒤 수"의 연산 횟수에 1을 더한 값들 중 제일 작은 값을 i의 연산 횟수로 지정한다.
    그렇게 설정하면 X에 가서 1부터 출발했을 때 연산 횟수를 구할 수 있다.
    입력 수가 3만이라서 BFS로 해도 시간 초과는 없을 거 같다. 다만 DP를 이용해 푸는 방법을 잘 알아두어야 한다
 """

import sys
from collections import deque
import time

X = int(sys.stdin.readline().rstrip())

""" approach 1 : BFS 사용하기 / 연산 결과를 node로, 연산을 edge로 하는 graph를 구성 """
def bfs(X):
    queue = deque([(X, 0)])
    graph = {}
    visited = {}
    visited[X] = True
    while queue:
        v, num = queue.popleft()
        if v not in graph:
            add_graph(v, graph)
        for neighbor in graph[v]:
            if neighbor == 1:
                return num + 1
            if neighbor not in visited:
                queue.append((neighbor, num+1))
                visited[neighbor] = True
    
    return 0

# 0: 5로 나눌 수 있으면 나누기 / 1: 3으로 나눌 수 있으면 나누기 / 2: 2로 나눌 수 있으면 나누기 / 3: 1 빼기
# 만약 해당사항이 없다면 0으로 가도록 만들어서 invalid 여부를 판단할 것
def add_graph(X, graph):
    tmp_list = [0,0,0,0]
    if X % 5 == 0: tmp_list[0] = X // 5
    if X % 3 == 0: tmp_list[1] = X // 3
    if X % 2 == 0: tmp_list[2] = X // 2
    tmp_list[3] = X -1
    graph[X] = tmp_list

start = time.time()

print("approach 1 :",bfs(X))

end = time.time()

print(f"> time:{end-start}")

""" approach 2 : DP / 책에서 Bottom-Up으로 해결한 풀이를 여기에 써봄 """
start = time.time()

d = [0]*30001

for i in range(2, X+1):
    d[i] = d[i-1]+1
    if i%2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i%3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i%5 == 0:
        d[i] = min(d[i], d[i//5]+1)
    
print("approach 2 :", d[i])
end = time.time()
print(f"> time:{end-start}")