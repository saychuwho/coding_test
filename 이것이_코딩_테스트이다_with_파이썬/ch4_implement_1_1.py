'''
나의 approach
    주어진 조건대로 일일이 움직여봤다
좀 더 좋은 approach
    list나 dictionary를 이용해 움직여야 하는 양을 미리 저장해놓는 방법도 있다.
'''

import sys

N = int(sys.stdin.readline())
plans = list(sys.stdin.readline().split())

dest_x = 1
dest_y = 1

# another solution.
dest_x_2 = 1
dest_y_2 = 1
move = {"L":(0,-1), "R":(0,1), "U":(-1,0), "D":(1,0)}

for plan in plans:
    move_x = 0
    move_y = 0
    if plan == "L":
        move_y = -1
    elif plan == "R":
        move_y = 1
    elif plan == "U":
        move_x = -1
    elif plan == "D":
        move_x = 1

    dest_x = dest_x + move_x if dest_x + move_x > 0 else dest_x
    dest_y = dest_y + move_y if dest_y + move_y > 0 else dest_y

    # another solution
    move_x_2 = move[plan][0]
    move_y_2 = move[plan][1]

    dest_x_2 = dest_x_2 + move_x_2 if dest_x_2 + move_x_2 > 0 else dest_x_2
    dest_y_2 = dest_y_2 + move_y_2 if dest_y_2 + move_y_2 > 0 else dest_y_2
    
    
print(dest_x, dest_y)
print(dest_x_2, dest_y_2)