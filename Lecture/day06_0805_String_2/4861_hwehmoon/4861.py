import sys
sys.stdin = open("input.txt", "r")

def finding_palindrome(N, M, arr):

    # 행 우선 탐색
    for i in range(N):
        for j in range(N - M + 1):

            s_num = M // 2 + j  # standard num index
            count = 0

            # N이 홀 수일 때 N-1, N+1 비교
            if M % 2 == 1:
                for k in range(M // 2):

                    # 기준점 좌우로 커지면서 값 같은지 비교
                    if arr[i][s_num + k] == arr[i][s_num - k]:
                        count += 1

                if count == M//2:
                    result = arr[i][j:j + M]
                    print(f'#{test_case} {"".join(result)}')

            # N이 짝수일 때 N-1 이랑 N이랑 비교
            elif M % 2 == 0:
                for k in range(M // 2):

                    # 기준점 좌우로 커지면서 값 같은지 비교
                    if arr[i][s_num + k] == arr[i][s_num - k - 1]:
                        count += 1

                if count == M//2:
                    result = arr[i][j:j + M]
                    print(f'#{test_case} {"".join(result)}')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    rev_arr = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            rev_arr[i][j] = arr[j][i]

    finding_palindrome(N, M, arr)
    finding_palindrome(N, M, rev_arr)
