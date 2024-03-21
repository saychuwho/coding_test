""" 
나의 approach
    BFS를 X에서 시작하고, BFS 하면서 X에서 거리가 K인 node들을 result에 포함한다
    BFS의 runtime이 O(N+M)이고, 어차피 오름차순으로 정렬하는 과정에서 O(NlogN)이기 때문에, runtime은 괜찮다.
 """

import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph = [[] for i in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

result = []
q = deque()
q.append((X, 0))
visited[X] = True
while q:
    node, length = q.popleft()
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            q.append((neighbor, length + 1))
            if length+1 == K:
                result.append(neighbor)


if not result:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)