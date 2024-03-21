""" 
나의 approach
    입력받은 list를 둘로 분리한 다음, list로 바꿔서 자리수별로 더한다.
 """

N = input()
mid = len(N) // 2
left = list(N[:mid])
right = list(N[mid:])

left_sum, right_sum = 0,0
for l, r in zip(left, right):
    left_sum += int(l)
    right_sum += int(r)

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")