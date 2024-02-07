# Python Basic 100 - 6095

board = [[0 for i in range(19)] for i in range(19)]

n = int(input())
for i in range(n):
    n, m = map(int, input().split())
    board[n-1][m-1] = 1

for i in range(19):
    for j in range(19):
        if j != 18:
            print(board[i][j], end=' ')
        else:
            print(board[i][j])