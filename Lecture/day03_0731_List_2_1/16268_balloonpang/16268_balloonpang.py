
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # 이거 무조건 익숙해지기
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 제로 패딩하기
    bubble_arr = [[0] * (M + 2) for _ in range(N + 2)]
    for i in range(N):
        for j in range(M):
            bubble_arr[i+1][j+1] = arr[i][j]

    di = [0, -1, 0, 1, 0]
    dj = [0, 0, 1, 0, -1]

    total = 0
    for i in range(N):
        for j in range(M):
            sum_v = 0
            for k in range(5):
                sum_v += bubble_arr[i+di[k]+1][j+dj[k]+1]
            if total < sum_v:
                total = sum_v
    print(f'#{test_case} {total}')
