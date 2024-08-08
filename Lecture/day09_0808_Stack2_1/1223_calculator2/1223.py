import sys
sys.stdin = open("input.txt", "r")

op_dict = {"*": 2, "+": 1}

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(input())

    stack = []
    operator = []

    # 후위 표기식으로 바꾸기
    for char in arr:
        if char.isdigit():
            stack.append(char)
        else:
            if not operator or op_dict[char] > op_dict[operator[-1]]:
                operator.append(char)
            elif op_dict[char] <= op_dict[operator[-1]]:
                stack.append(operator.pop())
                operator.append(char)
    
    stack.extend(operator[::-1])
    changed_arr = stack

    stack = []
    operator = []

    # 계산해주기
    for char in changed_arr:
        if char.isdigit():
            stack.append(int(char))
        else:
            end = stack.pop()
            start = stack.pop() 
            if char == "*":
                sum_v = start * end
                stack.append(sum_v)
            elif char == "+":
                sum_v = start + end
                stack.append(sum_v)

    print(f'#{tc} {stack[0]}')
