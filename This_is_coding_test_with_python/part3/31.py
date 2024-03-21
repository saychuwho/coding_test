""" 
나의 approach
    바로 왼쪽에서 왔을 때, 왼쪽 위에서 왔을 때, 왼쪽 아래에서 왔을 때를 경우의 수로 나누어서, 점화식을 세웠다
    근데 코드로 구현했을 때 계속해서 오답이 나오는데, 이 부분을 solution code를 보고 한번 어디서 잘못되었는지 찾아봐야 한다.
풀이 코드 분석
    일단은 column을 1에서 시작하나, 0에서 시작하나 일단 차이는 없다. 이전 코드에서는 내가 이거를 빼놨으니까.
    그리고 max 찾는 방식이 다르다 일단은. y의 제일 마지막 중에서 하나를 max로 잡는다. 
    왜냐하면 (0,0)에서 출발해서 도달할 수 있는 경우의 수는 제일 마지막 열밖에 없고, 중간에서 멈춘다면 절대로 최대값이 될 수 없다.
    조건식을 풀이 코드랑 동일하게 맞춰도 왜 두번째는 제대로 안나오는거지? 
    x의 순서랑 y의 순서를 바꾸니까 올바르게 나온다.... 왜?
    움직이는 방법을 고려했을 때, 열을 고정한 다음에 행별로 계산을 하는게 자연스러운 움직임이다!!!
    자연스러운 움직임을 고려해서 iteration을 돌려야 한다.....
 """


""" old code not get proper answer >> 정답 코드 참고해서 올바른 답을 만들어냄 """

def algorithm(case_list, x, y):
    gold_mine = [case_list[(i-1)*y:i*y] for i in range(1, x+1)]
    max_val = gold_mine[0][0]
    for j in range(1, y):
        for i in range(x):
            left_up, left_down = 0, 0
            left = gold_mine[i][j-1]
            if i != 0:
                left_up = gold_mine[i-1][j-1]
            if i != x-1:
                left_down = gold_mine[i+1][j-1]

            gold_mine[i][j] = gold_mine[i][j] + max(left, left_up, left_down)

            if gold_mine[i][j] > max_val:
                max_val = gold_mine[i][j]
    
    print(gold_mine)

    return max_val

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    case_list = list(map(int, input().split()))
    print(algorithm(case_list, x, y))


""" answer code: https://github.com/ndb796/python-for-coding-test/blob/master/16/1.py """

# # 테스트 케이스(Test Case) 입력
# for tc in range(int(input())):
#     # 금광 정보 입력
#     n, m = map(int, input().split())
#     array = list(map(int, input().split()))

#     # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
#     dp = []
#     index = 0
#     for i in range(n):
#         dp.append(array[index:index + m])
#         index += m

#     # 다이나믹 프로그래밍 진행
#     for j in range(1, m):
#         for i in range(n):
#             # 왼쪽 위에서 오는 경우
#             if i == 0:
#                 left_up = 0
#             else:
#                 left_up = dp[i - 1][j - 1]
#             # 왼쪽 아래에서 오는 경우
#             if i == n - 1:
#                 left_down = 0
#             else:
#                 left_down = dp[i + 1][j - 1]
#             # 왼쪽에서 오는 경우
#             left = dp[i][j - 1]
#             dp[i][j] = dp[i][j] + max(left_up, left_down, left)

#     result = 0
#     for i in range(n):
#         result = max(result, dp[i][m - 1])

#     print(result)

    