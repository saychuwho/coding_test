# Python Basic 100 - 6098

board = []

for _ in range(10):
    tmp_list = list(map(int, input().split()))
    board.append(tmp_list)

x, y = 1,1

while True:
    if board[x][y] == 2:
        board[x][y] = 9
        break

    board[x][y] = 9

    if board[x][y+1] != 1:
        y += 1
    elif board[x+1][y] == 1:
        break
    else:
        x += 1

for i in range(10):
    for j in range(10):
        if j != 9:
            print(board[i][j], end=' ')
        else:
            print(board[i][j])