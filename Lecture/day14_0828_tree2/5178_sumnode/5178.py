import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())

    h = [0] * (N+1)

    # M개 리프노드만큼 받기
    for _ in range(M):
        pos, data = map(int, input().split())
        # 저장
        h[pos] = data

    # N이 홀수일때
    if N%2 == 1:
        for i in range(N//2, 0, -1):
            h[i] = h[2*i] + h[2*i+1]

    # N이 짝수일때
    if N%2 == 0:
        h[N // 2] = h[N]
        for i in range(N//2-1, 0, -1):
            h[i] = h[2*i] + h[2*i+1]

    print(f'#{tc} {h[L]}')