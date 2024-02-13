import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline())))

# 앞의 두개 : 좌표 
queue = deque([(0,0)])