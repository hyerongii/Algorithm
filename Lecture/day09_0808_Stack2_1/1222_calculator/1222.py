import sys
sys.stdin = open("input.txt", "r")

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(input())
    
    stack = []
    operator = []

    # 후위 표기식으로 바꾸기
    for char in arr:
        if char.isdigit():
            stack.append(int(char))
        else:
            if not operator:
                operator.append(char)
            elif operator:
                stack.append(char)
    
    stack.extend(operator)
    changed_arr = stack
    
    # 후위 표기식에서 계산해주기
    stack = []
    operator = []
    
    for char in changed_arr:
        if type(char) == int:
            stack.append(char)
        else:
            if char == "+":
                end = stack.pop()
                start = stack.pop()
                sum_v = start + end
                stack.append(sum_v)

    print(f'#{tc} {stack[0]}')
