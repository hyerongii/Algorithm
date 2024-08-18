import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    pic = [list(map(int, input().split())) for _ in range(N)]
    # 행렬 탐색하면서 연속으로 1 오면 카운트 하기 (행 우선 탐색)
    max_len = 0
    for i in range(N):
        count_r = 1
        for j in range(M - 1):
            if pic[i][j] == 1 and pic[i][j + 1] == 1:
                count_r += 1
        if max_len < count_r:
            max_len = count_r
    # 전치행렬 만들어줌
    rev_arr = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            rev_arr[i][j] = pic[j][i]
    # 다시 탐색해서 카운트
    for i in range(M):
        count_c = 1
        for j in range(N - 1):
            if rev_arr[i][j] == 1 and rev_arr[i][j + 1] == 1:
                count_c += 1
        if max_len < count_c:
            max_len = count_c
    print(f'#{tc} {max_len}')