""" 
나의 approach
    뭔가 python 정렬 라이브러리를 잘 활용하면 깔끔하게 풀 수 있을 거 같은데, 떠오르지 않았다...
    일단 counting sort의 아이디어를 사용해, 국어 점수를 정렬하고, 국어 점수가 동일한 사람들끼리는 영어 점수를 그에 맞춰서 정렬하고... 이런 식으로 풀어보려고 했다.
    근데 영어 점수를 정렬하는 과정부터 막혀서, 시간안에 풀지는 못했다.
solution's approach
    역시 파이썬 정렬 라이브러리를 활용하는 문제였다.
    파이썬 정렬 라이브러리의 정확한 동작들을 다시 한번 정리해보자.
 """

""" old code that failed to solve in time """

"""
N = int(input())

korean = [[] for _ in range(101)]
english = [[] for _ in range(101)]
math = [[] for _ in range(101)]
info = {}

for _ in range(N):
    name, k, e, m = input().split()
    korean[int(k)].append(name)
    english[int(e)].append(name)
    math[int(m)].append(name)
    info[name] = (int(k), int(e), int(m))


for k_name_list in list(reversed(korean)):
    if not k_name_list:
        continue
    elif len(k_name_list) > 1:
        for k_name in k_name_list:
            pass
    else:
        print(k_name_list[0])
"""

""" solution code: https://github.com/ndb796/python-for-coding-test/blob/master/14/1.py """

n = int(input())
students = [] # 학생 정보를 담을 리스트

# 모든 학생 정보를 입력 받기
for _ in range(n):
    students.append(input().split())

'''
[ 정렬 기준 ]
1) 두 번째 원소를 기준으로 내림차순 정렬
2) 두 번째 원소가 같은 경우, 세 번째 원소를 기준으로 오름차순 정렬
3) 세 번째 원소가 같은 경우, 네 번째 원소를 기준으로 내림차순 정렬
4) 네 번째 원소가 같은 경우, 첫 번째 원소를 기준으로 오름차순 정렬
'''
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 정렬된 학생 정보에서 이름만 출력
for student in students:
    print(student[0])
