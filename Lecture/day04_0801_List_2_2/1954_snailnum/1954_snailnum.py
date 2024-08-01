import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    # 먼저 N 크기 배열 만들기
    blank_arr = [[0] * N for _ in range(N)]

    # 꼭짓점 만나면 방향 틀기
    # i 그대로 j 증가
    # i 증가 j 그대로
    # i 그대로 j 감소
    # i 감소 j 그대로

    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    i = 0
    j = 0
    idx = 0  # di, dj 인덱스 움직이기

    for num in range(1, N*N + 1):
        blank_arr[i][j] = num
        i += di[idx]
        j += dj[idx]

        # -,N에 도달하면 idx 움직이기
        if i < 0 or j < 0 or N <= i or N <= j or blank_arr[i][j] != 0 :
            i -= di[idx]
            j -= dj[idx]

            idx = (idx+1)%4   # 0,1,2,3,0,1,2,3,0,1,2,3 나와야함
            i += di[idx]
            j += dj[idx]

    print(f'#{test_case}')
    for data in blank_arr:
        print(f'{" ".join(list(map(str, data)))}')


