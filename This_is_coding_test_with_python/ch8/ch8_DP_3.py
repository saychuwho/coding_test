""" 
나의 approach
    생각이 잘 안난다... 이거는 책을 보고 점화식 세우는 감을 잡아야 할 듯
책의 approach
    특정 i번째 창고를 털 때, i번째를 터는 경우와, i번째를 안 터는 경우로 나누어서 생각해보면 된다
    이거 knapsack problem 하고 점화식 세우는게 비슷하다. 책 풀이를 보니까
    책 풀이를 써보면서 이해해보고, 탑다운으로 다시 식을 세워보자
 """

""" approach 1 : bottom-up, from book """
n = int(input())

array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(f"approach 1:{d[n-1]}")

""" approach 2: top-down """

d_2 = [0] * 100

d_2[0] = array[0]
d_2[1] = max(array[0], array[1])

def top_down(d, i):
    global array
    if d[i] != 0:
        return d[i]
    
    return max(top_down(d, i-1), top_down(d, i-2) + array[i])

print(f"approach 2:{top_down(d_2, n-1)}")