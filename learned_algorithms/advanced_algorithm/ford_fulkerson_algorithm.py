def BFS(graph, s, t, parent):
    # Return True if there is node that has not iterated.
    visited = [False] * len(graph)
    queue = []
    queue.append(s)
    visited[s] = True
 
    while queue:
        u = queue.pop(0)
        for neighbor in range(len(graph[u])):
            if visited[neighbor] is False and graph[u][neighbor] > 0:
                queue.append(neighbor)
                visited[neighbor] = True
                parent[neighbor] = u
 
    return True if visited[t] else False
 
 
def FordFulkerson(graph, source, sink):
    parent = [-1] * (len(graph)) # This array is filled by BFS and to store path
    max_flow = 0

    # if while ends, that means there are cuts between source and sink
    while BFS(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
 
        # Find the minimum value in select path
        while s != source:    
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
 
        max_flow += path_flow
        v = sink
 
        # making residual graph
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow # this decrease the original edge's flow lower
            graph[v][u] += path_flow # this act like making residual graph
            v = parent[v]

    return max_flow
 
# graphs described with adjacency matrix
graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0],
]
 
source, sink = 0, 5
print(FordFulkerson(graph, source, sink))