import sys
sys.stdin = open("input.txt", "r")

def finding_longest_palindrome(M, arr):

    for i in range(N):
            for j in range(N-M+1):
                if arr[i][j] == arr[i][j+M-1]:
                    for k in range(1, M//2):
                        if arr[i][j+k] != arr[i][j+M-1-k]:
                            break
                    else: 
                        return True
                
            for j in range(N-M+1):
                if arr[j][i] == arr[j+M-1][i]:
                    for k in range(1, M//2):
                        if arr[j+k][i] != arr[j+M-1-k][i]:
                            break
                    else:
                        return True
    return False

T = 10
for test_case in range(1, T+1):
    tc = int(input())
    N = 100
    arr = [input() for _ in range(N)]
    for M in range(N, -1, -1):
        if finding_longest_palindrome(M, arr):
            print(f'#{tc} {M}')
            break