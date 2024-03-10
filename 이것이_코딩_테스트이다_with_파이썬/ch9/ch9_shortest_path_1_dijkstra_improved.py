""" example code from book """

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 현재 node가 이미 처리된 적이 있는 경우
        # heap에 집어넣어진 뒤에 처리가 되어서 dist보다 작은 경우니까, 이미 방문을 한 적이 있다는 뜻이다.
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            # now를 겇쳐서 가는 경우가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])