'''
나의 approach
    모든 node에 대해서 dfs를 돌려보면 되는 걸로 만들었다.
    붙어있는 형태로 들어오면 split이 안되길래 그냥 수동으로 찢었다
    방문한적이 있거나 칸막이면 False, 좌표 조건에서 벗어나도 False를 반환하도록 했다
    성공적으로 탐험을 완료한 node이면 True를 반환
보완할 수 있는 부분
    그냥 map(int, input())을 하면 int 형태의 list가 된다. 이거는 알아두자.
    이외에는 내 코드랑 다른점은 없는듯.
'''

import sys

N, M = map(int, sys.stdin.readline().split())
ice_case = []
for _ in range(N):
    tmp_str = sys.stdin.readline()
    tmp_row = []
    for l in tmp_str:
        tmp_row.append(l)

    '''
    여기서 다음과 같이 받을 수도 있음
    ice_case.append(list(map(int, sys.stdin.readline())))
    '''

    ice_case.append(tmp_row)

def dfs(x, y):
    if x < 0 or y < 0 or x >= N or y >= M:
        return False
    elif ice_case[x][y] == '1':
        return False
    
    ice_case[x][y] = '1'
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)

    return True

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)