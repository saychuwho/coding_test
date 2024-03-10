""" 
나의 approach
    다익스트라를 두번 사용하면 되는게 아닌가?
    양방향 조건에 항상 신경쓰도록....
책의 approach
    플로이드 워샬을 쓰면 한큐에 구해지는데 궅이?
    두 가지 경우를 모두 작성해보자. 코드 작성하는데 익숙해질 수 있도록
 """

import heapq

INF = int(1e9)

N, M = map(int, input().split())

graph_dijkstra = [[] for _ in range(N+1)]
graph_FW = [[INF]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph_dijkstra[a].append(b)
    graph_dijkstra[b].append(a)
    graph_FW[a][b] = 1
    graph_FW[b][a] = 1

X, K = map(int, input().split())


""" floyd-warshal """

for i in range(N+1):
    graph_FW[i][i] = 0

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph_FW[a][b] = min(graph_FW[a][b], graph_FW[a][k]+graph_FW[k][b])


to_date = graph_FW[1][K]
to_work = graph_FW[K][X]


if to_date == INF or to_work == INF:
    print(-1)
else:
    print(to_date + to_work)


""" dijkstra """
distance_to_date = [INF]*(N+1)
distance_to_work = [INF]*(N+1)

def dijkstra(start, dest, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for neighbor in graph_dijkstra[now]:
            cost = dist + 1
            if cost < distance[neighbor]:
                distance[neighbor] = cost
                heapq.heappush(q, (cost, neighbor))
    
    return distance[dest]

to_date = dijkstra(1, K, distance_to_date)
to_work = dijkstra(K, X, distance_to_work)


if to_date == INF or to_work == INF:
    print(-1)
else:
    print(to_date + to_work)