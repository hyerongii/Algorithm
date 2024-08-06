import sys
sys.stdin = open("input.txt", "r")

def finding_palindrome(N, arr):

    # 행 우선 탐색
    for i in range(N):
        # 길이 N-1 .. 1 까지의 윈도우 만들기
        for M in range(N, 1, -1):  
            # 시작좌표, 차례대로 자르기
            for j in range(N-M+1):

                word = arr[i][j:j + M]

                left, right = 0, len(word) -1
    
                while left < right:
                    if word[left] != word[right]:
                        return False
                    left += 1
                    right -= 1
                
                return M

T = 10

for test_case in range(1, T + 1):
    tc = int(input())
    N = 100
    arr = [list(input()) for _ in range(100)]

    rev_arr = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            rev_arr[i][j] = arr[j][i]

    result1 = finding_palindrome(N, arr)
    result2 = finding_palindrome(N, rev_arr)

    if result1 > result2:
        print(f'#{test_case} {result1}')
    else:
        print(f'#{test_case} {result2}')
