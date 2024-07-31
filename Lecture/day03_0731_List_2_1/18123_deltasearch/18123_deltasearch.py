import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # ni - i, nj - j -> abs 처리
    total = 0
    for i in range(N):
        for j in range(N):
            sum_v = 0
            for k in range(4):
                ni = i+di[k]
                nj = j+dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    sum_v += abs(arr[i][j] - arr[ni][nj])
            total += sum_v

    print(f'#{test_case} {total}')

