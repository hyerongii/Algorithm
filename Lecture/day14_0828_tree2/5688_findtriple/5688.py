import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    if N > 1:
        for i in range(2, 1000001):
            if N == i**3:
                result = i
                break
            else:
                result = -1
    else:
        result = 1
    print(f'#{tc} {result}')