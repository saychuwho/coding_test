""" example code from book """

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소를 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0] # pivot은 첫 번째 원소
    tail = array[1:] # pivot을 제외한 리스트

    left_side = [x for x in tail if x<= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))