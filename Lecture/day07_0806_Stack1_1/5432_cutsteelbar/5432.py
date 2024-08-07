import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    string = input()
    stack = []

    # 레이저 뽑아내서 * 변환
    for i in range(len(string)):
        if not stack or string[i] != ")" or stack[-1] != "(" :
            stack.append(string[i])
        else:
            stack[-1] = 1 

    stack = []
    sum_v = 0

    for i in range(len(string)):
        if not stack or stack[-1] != "(" or string[i] != 1:
            sum_v += 1
            print(sum_v)
        else:
            stack.pop()
    
    

    print(stack)