import sys
sys.stdin = open("input.txt", "r")

T = 10
for tc in range(1, T+1):
    N, string = input().split()
    N = int(N)
    string = list(string)

    stack = ['*']

    for i in range(N):

        if stack[-1] != string[i]:
            stack.append(string[i])
        else:
            stack.pop()
    
    result = "".join(stack[1:])

    print(f'#{tc} {result}')
