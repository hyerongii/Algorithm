import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    stack = []
    operator = ["*", "/", "+", "-"]
    try:
        for char in arr:
            if char == ".":
                if len(stack) > 1:
                    print(f'#{tc} error')
                    break
                last_num = stack.pop()
                print(f'#{tc} {int(last_num)}')
            if char.isdigit():
                stack.append(int(char))
            elif char in operator:
                # 먼저 꺼낸게 뒤에
                end = stack.pop()
                # 나중에 꺼낸게 앞에
                start = stack.pop()
                # 계산식 
                if char == "*":
                    sum_v = start * end
                elif char == "/":
                    sum_v = start / end
                elif char == "+":
                    sum_v = start + end
                elif char == "-":
                    sum_v = start - end
                # 계산값 stack에 다시 넣기
                stack.append(sum_v)
    except:
        print(f'#{tc} error')

