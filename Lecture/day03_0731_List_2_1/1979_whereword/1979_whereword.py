
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    # 이거 무조건 익숙해지기
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 0, 0]
    dj = [0, 1, 2]

    ei = [0, 1, 2]
    ej = [0, 0, 0]

    count = 0
    window_list = []
    for i in range(N):
        for j in range(N):
            window_list.append(arr[i])




    print(f'#{test_case} {count}')