""" 
나의 approach
    kruskal algorithm을 사용하면 된다.
    kruskal을 한번 돌린 다음에, 제일 비용 큰 edge를 마지막에 지우면 마을이 분리된다
 """

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())

parent = [0] * (N+1)
edges = []
result = 0
max_edge_weight = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

for i in range(N+1):
    parent[i] = i

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        if max_edge_weight < cost:
            max_edge_weight = cost

print(result - max_edge_weight)