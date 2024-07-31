import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sum_diagonal = 0
    for i in range(N):
        sum_diagonal += arr[i][i]
        sum_diagonal += arr[i][N-i-1]
    # N이 홀수일 때, 중간값 제거
    if N % 2 == 1:
        sum_diagonal -= arr[N//2][N//2]
    print(f'#{test_case} {sum_diagonal}')