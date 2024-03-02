""" 
나의 approach
    문제를 해결할 방법이 막 안떠오르면, 그냥 책의 solution을 일단 한번 보고, top-down 코드로 바꿔보는 작업을 해보자
    2 x N 이었네... 내가 너무 복잡하게 생각하고 있었다
 """

""" approach 1: bottom-up """

n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, n+1):
    d[i] = (d[i-1] + 2 * d[i-2]) % 796796

print(f"approach 1: {d[n]}")

""" approach 2: top-down """
d_2 = [0] * 1001

d_2[1] = 1
d_2[2] = 3

def top_down(d, i):
    if d[i] != 0:
        return d[i]
    
    return (top_down(d, i-1) + 2*top_down(d, i-2)) % 796796

print(f"approach 2: {top_down(d, n)}")