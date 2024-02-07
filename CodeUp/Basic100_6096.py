# Python Basic 100 - 6096

board = []

for i in range(19):
    tmp_list = list(map(int, input().split()))
    board.append(tmp_list)

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    
    for j in range(19):
        if board[x-1][j] == 0:
            board[x-1][j] = 1
        else:
            board[x-1][j] = 0
    
    for j in range(19):
        if board[j][y-1] == 0:
            board[j][y-1] = 1
        else:
            board[j][y-1] = 0

for i in range(19):
    for j in range(19):
        if j != 18:
            print(board[i][j], end=' ')
        else:
            print(board[i][j])