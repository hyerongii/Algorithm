import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Q_num = list(input().split())

    # N개의 숫자로 이루어진 수열을 M번 이동
    for _ in range(M):
        Q_num.append(Q_num[0])
        Q_num.pop(0)

    print(f'#{tc} {Q_num[0]}')

