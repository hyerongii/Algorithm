import sys; sys.stdin = open('1215.txt')

for tc in range(1, 11):

    N = 8
    M = int(input())
    arr = [input() for _ in range(N)]

    cnt = 0
    # 모든 행에 대해서 반복
    for row in range(N):
        # arr[row]행에서 길이 M인 회문을 찾기
        for s in range(0, N-M + 1):
            e = s + M - 1
            # 회문체크
            for i in range(M//2):
                if arr[row][s+i] != arr[row][e-i]:
                    break
            else:
                cnt += 1

    # 모든 열에 대해서 반복
    for col in range(N):
        # arr[][col]열에서 길이 M인 회문을 찾기
        for s in range(0, N-M + 1):
            e = s + M - 1
            # 회문체크
            for i in range(M//2):
                if arr[s+i][col] != arr[e-i][col]:
                    break
            else:
                cnt += 1

    print(f'#{tc} {cnt}')
