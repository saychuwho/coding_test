'''
나의 approach
    나이트가 이동 가능한 모든 경우의 수를 move에 담아둔 다음에, move를 for문 돌려가면서 검사함
'''

import sys

cord = sys.stdin.readline()

row = int(cord[1])
col = ord(cord[0]) - 96

move = [(2, -1),(2,1),(-1,2),(1,2),(-2,-1),(-2,1),(1,-2),(-1,-2)]

counter = 0

for case in move:
    tmp_row = row + case[0]
    tmp_col = col + case[1]
    if tmp_row <= 0 or tmp_col <= 0 or tmp_row > 8 or tmp_col > 8:
        continue
    counter += 1

print(counter)