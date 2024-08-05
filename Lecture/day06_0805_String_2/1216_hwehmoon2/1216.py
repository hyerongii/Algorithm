import sys
sys.stdin = open("input.txt", "r")

def finding_palindrome(N, arr):

    # 행 우선 탐색
    for i in range(N):
        # 길이 1 ~ N+1 까지의 윈도우 만들기
        for M in range(1, N+1):  
            # 시작좌표, 차례대로 자르기
            for j in range(N-M+1):

                s_num = M // 2 + j  # standard num index
                count = 0
                max_c = 1

                # N이 홀수일 때 N-1, N+1 비교
                if M % 2 == 1:
                    for k in range(M//2):

                        # 기준점 좌우로 커지면서 값 같은지 비교
                        if arr[i][s_num + k] == arr[i][s_num - k]:
                            count += 1

                # N이 짝수일 때 N-1 이랑 N이랑 비교
                elif M % 2 == 0:
                    for k in range(M // 2):

                        # 기준점 좌우로 커지면서 값 같은지 비교
                        if arr[i][s_num + k] == arr[i][s_num - k -1]:
                            count += 1
                        
                if count == M//2:
                    result = arr[i][j+1 : j + M - 1]
                    print(result)

                    if max_c < len(result):
                        max_c = len(result)

    return max_c

T = 10

for test_case in range(1, T + 1):
    tc = int(input())
    N = 100
    arr = [list(input()) for _ in range(100)]

    rev_arr = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            rev_arr[i][j] = arr[j][i]

    result1 = finding_palindrome(N, arr)
    result2 = finding_palindrome(N, rev_arr)

    if result1 > result2:
        print(f'#{test_case} {result1}')
    else:
        print(f'#{test_case} {result2}')
