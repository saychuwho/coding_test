# recurssion version DFS

UNVISITED = 0
IN_PROGRESS = 1
DONE = 2

def DFS(graph, progress, start_time, finish_time, w, current_time):
    start_time[w] = current_time
    current_time += 1
    progress[w] = IN_PROGRESS

    print(f"{w} is in progress with current time {current_time}")

    for v in graph[w]:
        if progress[v] == UNVISITED:
            current_time = DFS(graph, progress, start_time, finish_time, v, current_time)
            current_time += 1
    finish_time[w] = current_time
    progress[w] = DONE

    print(f"{w} is finished with current time {current_time}")

    return current_time

# empty the zero
graph = [[],
         [2, 4, 6],
         [],
         [5],
         [3,5],
         [],
         []]

progress = [0] * len(graph)
start_time = [0] * len(graph)
finish_time = [0] * len(graph)
current_time = 0

DFS(graph, progress, start_time, finish_time, 1, current_time)