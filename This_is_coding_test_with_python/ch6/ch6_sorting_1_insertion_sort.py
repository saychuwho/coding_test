""" example code from book 
https://github.com/ndb796/python-for-coding-test/blob/master/6/3.py"""

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)): # 첫 번째 데이터는 이미 정렬되어 있다 가정하고 두 번째 데이터부터 정렬을 시작한다
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하며 반복하는 문법
        if array[j] < array[j-1]: # i번째 원소를 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)