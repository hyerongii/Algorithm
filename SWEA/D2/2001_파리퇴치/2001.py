import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 파리 잡아줄 arr
    catch_arr = [[0]*M for _ in range(M)]
    max_v = arr[0][0]
    # N배열 만들어주고 M 윈도우로 돌려주기
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_v = 0
            for k in range(M):
                for l in range(M):
                    sum_v += arr[i+k][j+l]

            if sum_v > max_v:
                max_v = sum_v

    print(f'#{tc} {max_v}')





