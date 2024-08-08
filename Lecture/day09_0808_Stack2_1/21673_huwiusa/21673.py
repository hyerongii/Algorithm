import sys
sys.stdin = open("input.txt", "r")

cal = {"+": 1,
        "-": 1,
        "*": 2,
        "/": 2}

T = int(input())
for tc in range(1, T + 1):
    arr = input()
    stack = []
    operator = []

    for char in arr:
        if char not in cal.keys():
            stack.append(char)
        else:
            if not operator or cal[char] > cal[operator[-1]]:
                operator.append(char)
            elif cal[char] <= cal[operator[-1]]:
                stack.append(operator.pop())
                operator.append(char)

    stack.extend(operator[::-1])
    print(f'#{tc} {"".join(stack)}')