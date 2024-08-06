import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    string = list(input())
    stack = []

    # 레이저 뽑아내서 * 변환
    for i in range(len(string)):
        if not stack or string[i] != ")" or stack[-1] != "(" :
            stack.append(string[i])
        else:
            stack[-1] = '*'    
