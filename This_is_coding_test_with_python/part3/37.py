""" 
나의 approach 
    플로이드 워셜을 알고 있는지를 물어보는 기초적인 문제
    플로이드 워셜은 점화식을 기억하기 매우 쉬우니까, 잘 알아두고 있자.
 """

N = int(input())
M = int(input())

INF = int(1e9)

graph = [[INF for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    graph[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()