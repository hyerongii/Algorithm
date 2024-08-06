import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # 입력문자 수정해야하기 때문에,, list로 변환
    string = input()
    stack = []

    for i in range(len(string)):
        if not stack or stack[-1] != string[i]:
            stack.append(string[i])
        else:
            stack.pop()
            
    print(f'#{test_case} {len(stack)}')
