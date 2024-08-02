import sys
sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T+1):
    tc = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 배열 끝에 2 값이 최종 도착지
    # 올라가면서 찾는다!!

    # zero padding 하기.. 0으로 다 막아주기
    real_arr = [[0] * (N+2) for _ in range(N+2)]  # 0~101 102개
    for i in range(N):
        for j in range(N):
            real_arr[i+1][j+1] = arr[i][j]

    # 출발점 찾기, 출발점에서 시작하기 start point : sp
    sp_i = N
    sp_j = real_arr[N].index(2)

    while sp_i != 0:
        if real_arr[sp_i][sp_j-1] == 1:
            real_arr[sp_i][sp_j] = 0
            sp_j -= 1
        elif real_arr[sp_i][sp_j+1] == 1:
            real_arr[sp_i][sp_j] = 0
            sp_j += 1
        else:
            sp_i -= 1

    print(f'#{test_case} {sp_j-1}')