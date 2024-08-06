import sys
sys.stdin = open("input.txt", "r")

def pascal(n):

    stack = []

    if n == 1:
        return [1]
    
    elif n > 2:
        for _ in range(n):
            stack.append(1)
            stack.append(stack[-1]+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    for _ in range(N):
        print(pascal())

    print(f'#{tc}')
    print(pascal(N)) # 함수 넣기
