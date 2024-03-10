""" 
나의 approach
    그냥 다익스트라를 돌린 다음에, max값을 걸리는 시간으로, INF 인 개수를 빼면 될거 같음
    정확히는, n+1에서 INF의 수만큼 빼면 될 듯
    아니다. index 0이 무조건 INF이기는 하지만, 메시지를 보내는 도시도 빼야 하니까, 그냥 N에서 빼면 된다
 """

import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

N, M, C = map(int, input().split())

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

q = []
heapq.heappush(q, (0, C))
distance[C] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for neighbor, n_dist in graph[now]:
        cost = dist + n_dist
        if cost < distance[neighbor]:
            distance[neighbor] = cost
            heapq.heappush(q, (cost, neighbor))

total_time = 0
cities = N
for time_spent in distance:
    if time_spent == INF:
        cities -= 1
    else:
        total_time = max(total_time, time_spent)

print(cities, total_time)