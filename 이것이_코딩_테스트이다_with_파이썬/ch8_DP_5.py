""" 
나의 approach
    알고리즘 수업 때 했던 knapsack problem하고 비슷한거 같아서 그거를 바탕으로 sub-problem을 구성해봤다
    돈 x를 채우는 optimal한 화폐 개수를 N이라 하고, 화폐 종류를 w_i라 했을 때, N[x] = min_i{N[x], N[X - w_i]+1}이다
    다양한 예외조건들은 주석에 적어뒀다
책의 approach
    내 approach랑 비슷한 부분이 있지만, 다른 부분도 있다.
    단위별로 iteration을 도는 거랑, 불가능한 경우의 수를 매우 큰 수로 잡아서 나처럼 min을 고려해야 하는 경우, 아닌 경우의 코드가 없다.
 """

""" my approach """

money_num, X = map(int, input().split())
moneys = []
N = [0] * 10001
for _ in range(money_num):
    tmp_money = int(input())
    moneys.append(tmp_money)
    N[tmp_money] = 1

# bottom-up
for i in range(X+1):
    #print(f"i: {i}")
    for money in moneys:
        #print(f"> money: {money}")
        if i - money < 0:
            continue
        # if N[i-money] = 0이면, i-money에는 경우의 수가 아예 없다는 뜻이니 고려하면 안된다
        if N[i] != 0 and N[i-money] != 0:
            N[i] = min(N[i], N[i - money] + 1)
        elif N[i] == 0 and N[i-money] != 0:
            N[i] = N[i - money] + 1
        #print(f">> N[{i}]: {N[i]}")

if N[X] == 0: print(-1)
else: print(N[X])

""" book approach """

d = [10001] * (X + 1)

d[0] = 0
for i in range(money_num):
    for j in range(moneys[i], X+1):
        # 애초에 불가능한 경우를 매우 큰 수로 잡았기 때문에 min을 써야 하는 경우와 안써야 하는 경우로 안 나눠도 된다.
        if d[j-moneys[i]] != 10001:
            d[j] = min(d[j], d[j-moneys[i]] + 1)

if d[X] == 10001: print(-1)
else: print(d[X])