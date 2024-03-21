""" 
나의 풀이
    서로소 알고리즘을 잘 활용하면 된다.
 """

def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    if parent[a] < parent[b]:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]


N, M = map(int, input().split())

parent = [0]*(N+1)
for i in range(1, N+1):
    parent[i] = i

for i in range(1, N+1):
    edges = [0]
    edges.extend(list(map(int, input().split()))) 
    for j in range(1, N+1):
        if edges[j] == 0:
            continue
        union(parent, i, j)

plans = list(map(int, input().split()))
group = find(parent, plans[0])

is_available = True
for city in plans:
    if group != find(parent, city):
        is_available = False
        break

if is_available:
    print("YES")
else:
    print("NO")