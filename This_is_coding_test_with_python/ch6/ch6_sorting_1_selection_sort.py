""" example code from book 
https://github.com/ndb796/python-for-coding-test/blob/master/6/1.py 
"""

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        # min_index 찾기
        if array[min_index] > array[j]:
            min_index = j
        
    # swap
    array[i], array[min_index] = array[min_index], array[i]

print(array)