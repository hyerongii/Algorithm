import sys
sys.stdin = open("input.txt", "r")

# 나는 계속 1차원 배열로 생각함,,,
# 2차원 배열로 생각하기

# 점화식으로 생각해주기 
# dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 파스칼 출력 형태로 배열 틀 값이 모두 1인거로 생성
    arr = [[0] * N for _ in range(N)]
    print(f'#{tc}')

    # 2부터 더해짐
    for i in range(N):
        for j in range(i+1):
            if j == 0 and i == 0:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
            print(arr[i][j], end=" ")
        print()
