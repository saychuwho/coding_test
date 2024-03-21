""" 
나의 approach
    0과 1의 묶음 중 더 적은 묶음을 바꾸면 된다를 기본적인 아이디어로 생각함
 """

S = input()

counter = 0
res_list = [1,0]
for i in range(1, len(S)):
    if S[i-1] != S[i]:
        res_list[counter % 2] += 1
        counter += 1

print(min(res_list))