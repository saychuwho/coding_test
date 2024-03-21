UNVISITED = 0
IN_PROGRESS = 1
DONE = 2

# 이 방식은 좀 비효율적인거 같다. DFS_with_time.py에서 처럼 노드를 숫자로 표현하는 방식이 좀 더 효율적인듯. 
# 그냥 pseudo code 그대로 구현할 수 있다는 장점은 있는듯. class 연습삼아 이렇게 짜봤다 하자.
class Node:
    def __init__(self, name: str=""):
        self.name = name
        self.status = UNVISITED
        self.start_time = 0
        self.finish_time = 0
        self.neighbors = []

    def __repr__(self) -> str:
        return self.name


def DFS(u: Node, cur_time, topological_list: list):
    u.start_time = cur_time
    cur_time += 1
    u.status = UNVISITED
    for v in u.neighbors:
        cur_time = DFS(v, cur_time, topological_list)
        cur_time += 1
    u.finish_time = cur_time
    u.status = DONE
    topological_list.append(u)
    return cur_time

# same as the pseudo code

dpkg = Node("dpkg")
tar = Node("tar")
coreutils = Node("coreutils")
libz2 = Node("libz2")
multisearch = Node("multisearch")
libselinux = Node("libselinux")

dpkg.neighbors = [tar, coreutils, multisearch]
libz2.neighbors = [libselinux]
coreutils.neighbors = [libz2, libselinux]

topological_list = []
cur_time = 0
DFS(dpkg, cur_time, topological_list)

print(topological_list)
