
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # 이거 무조건 익숙해지기
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    total = 0
    for i in range(N):
        for j in range(M):
            l = arr[i][j] 
            sum_v = l
            for add in range(1, l+1):  
                for k in range(4): 
                    if 0 <= i+di[k]*add < N and 0 <= j+dj[k]*add < M:
                        sum_v += arr[i+di[k]*add][j+dj[k]*add]
            if total < sum_v:
                total = sum_v
    print(f'#{test_case} {total}')