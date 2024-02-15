'''
나의 approach 
    bfs에서 현재 이 노드의 depth?를 graph[x][y]에 저장해둠. 
    그 노드를 부른 노드의 graph[x][y]값에 1을 더한 식으로
    visited는 그냥 2차원 배열을 하나 선언함. 어차피 메모리도 그렇게 부족하지는 않을거 같았음
    나머지는 이전 문제에서 사용했던 dx, dy정도? 이 테크닉은 grid 환경에서 자주 사용될 거 같다. 익혀둬야 함

'''

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

visited = [[False for _ in range(M)] for _ in range(N)]

# 위, 오른쪽, 아래, 왼쪽 순서대로
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    queue = deque()
    queue.append([0,0])
    visited[0][0] = True
    while queue:
        
        # original code 
        """
        v = queue.popleft()
        v_x = v[0]
        v_y = v[1] 
        """

        # revised code
        v_x, v_y = queue.popleft()
        
        for i in range(4):
            v_nei_x = v_x + dx[i]
            v_nei_y = v_y + dy[i]
            if v_nei_x < 0 or v_nei_y < 0 or v_nei_x >= N or v_nei_y >= M:
                continue
            elif graph[v_nei_x][v_nei_y] == 0:
                continue
            if not visited[v_nei_x][v_nei_y]:
                queue.append([v_nei_x, v_nei_y])
                graph[v_nei_x][v_nei_y] = graph[v_x][v_y] + 1
                visited[v_nei_x][v_nei_y] = True
                if v_nei_x == N - 1 and v_nei_y == M - 1:
                    return True
                
    return False

bfs()

print(graph[N-1][M-1])
