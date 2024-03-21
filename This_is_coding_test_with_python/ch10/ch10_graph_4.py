""" 
나의 approach
    topological ordering을 이용한다
    queue에 집어넣을 때, 이전 단계 과목의 시간을 현재 과목 시간에 더해야 한다
 """

from collections import deque
import copy

N = int(input())

graph = [[] for _ in range(N+1)]
lecture_time = [0] * (N+1)
indegree = [0] * (N+1)

for i in range(1, N+1):
    order_info = list(map(int, input().split()))
    lecture_time[i] = order_info[0]
    for j in range(1, len(order_info)-1):
        graph[order_info[j]].append(i)
        indegree[i] += 1


result = copy.deepcopy(lecture_time)
q = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    
    for i in graph[now]:
        result[i] = max(result[i], result[now] + lecture_time[i])
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)
            
for i in range(1, N+1):
    print(result[i])