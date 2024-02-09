# Python Basic 100 - 6097

h, w = map(int, input().split())
n = int(input())

board = [[0 for _ in range(w)] for _ in range(h)]

for _ in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for i in range(l):
            board[x-1][y-1+i] = 1
    else:
        for i in range(l):
            board[x-1+i][y-1] = 1
    
for i in range(h):
    for j in range(w):
        if j == w-1:
            print(board[i][j])
        else:
            print(board[i][j], end=' ')
