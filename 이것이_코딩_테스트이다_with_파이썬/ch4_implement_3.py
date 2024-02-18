'''
나의 approach
    - 동서남북 움직일 수 있는 곳을 move_x, move_y에 지정해두었다
    - 왼쪽으로 바라보는 방향 회전 : (player_look + 3) % 4
    - 반대로 움직이는 방향 찾기 : (player_look + 6) % 4
    - for 문을 5번 돈다 
        - 최초 방문 (i==1) : 현재 위치를 map_matrix에 방문한 것으로 처리 (2를 대입)
        - 모든 방향을 검토했는데 방문했거나 바다여서 최초 바라보는 방향으로 온 경우 (i==4) : 뒤로 이동. 이때, 뒤가 바다이면 is_continue = False로 바꿔 종료
        - 나머지 : player_look 방향으로 한칸 갔을 때 전진할 수 있으면 전진하고 아니면 방향 회전 후 다음 iter 수행
        - 이동할 때 마다 counter += 1

다른 approach
    - 책의 approach는 대부분 비슷한데, 나는 for문을 한번 더 쓴거고, 여기는 while 문 하나로 처리했다
    - 회전을 할 때 책의 approch는 함수를 하나 만들어서 처리했다. 나 같은 경우에는 나머지를 이용해서 수학적으로 계산한 거고
    - 책의 approach는 방문한 위치 저장을 다른 2차원 배열을 만들어서 저장하고, 나는 map_matrix에 합쳐서 사용했다

문법적 오류
    - map_matrix를 최초에 map이라고 이름을 지어서 map()이 정상적으로 동작하지 않았었다. 변수 이름은 내장함수랑 겹치지 않게 설정하자
    - split()을 뒤에 빠트리지 말자
'''

import sys

N, M = map(int, sys.stdin.readline().split())
player_x, player_y, player_look = map(int, sys.stdin.readline().split())

map_matrix = []

for _ in range(N):
    tmp_list = list(map(int, sys.stdin.readline().split()))
    map_matrix.append(tmp_list)

move_x = [-1,0,1,0]
move_y = [0,1,0,-1]

counter = 1
is_continue = True
while is_continue:
    for i in range(5):
        if i == 1:
            map_matrix[player_x][player_y] = 2
        elif i == 4:
            tmp_d = (player_look + 6) % 4
            player_x += move_x[tmp_d]
            player_y += move_y[tmp_d]
            
            if map_matrix[player_x][player_y] == 1:
                is_continue = False
                break
            
            counter += 1
        else:
            player_look = (player_look + 3) % 4
            tmp_x = player_x + move_x[player_look]
            tmp_y = player_y + move_y[player_look]
            if map_matrix[tmp_x][tmp_y] == 1 or map_matrix[tmp_x][tmp_y] == 2:
                continue
            else:
                player_x = tmp_x
                player_y = tmp_y
                counter += 1
                break
        

print(counter)