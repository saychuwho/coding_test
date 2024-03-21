""" example code from book 
https://github.com/ndb796/python-for-coding-test/blob/master/10/6.py"""

""" DFS를 활용한 topological sorting도 있다. 수업시간에 배운. 그거는 나중에 따로 정리해보자 """

from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v+1)

graph = [[] for i in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()