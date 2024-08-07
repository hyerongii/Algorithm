import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    string = input()

    stack = []
    sum_v = 0

    for i in range(len(string)):
        if string[i] == "(" :
            stack.append("(")
        else:
            stack.pop()
            if string[i-1] == "(":
                sum_v += len(stack)
            else:
                sum_v += 1

    print(f'#{tc} {sum_v}')


'''
다른 방법

cnt = 0  # 막대수
ans = 0

for i in range(len(string)):
    if string[i] == "(":
        cnt += 1
    elif string[i-1] == "(":
        cnt -= 1
        ans += cnt
    else:
        cnt -= 1
        ans += 1

print(f'#{tc} {ans}')        
'''