""" example code from book 
https://github.com/ndb796/python-for-coding-test/blob/master/6/6.py"""

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count = [0] * (max(array) + 1) # max()는 O(N)에 수행할 수 있다

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')

""" 내가 좀 고쳐본 코드. 좀 더 pythonic한 코드? """
print()

count_2 = [0] * (max(array) + 1)

for number in array:
    count_2[number] += 1

for i, count in enumerate(count_2):
    for j in range(count):
        print(i, end=' ')
