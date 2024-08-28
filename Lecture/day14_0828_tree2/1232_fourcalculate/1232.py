import sys
sys.stdin = open("input.txt", "r")

def cal(left, right, operator):
    if operator == "*":
        return left * right
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "/":
        return left / right

def search(node):
    # 만약 연산자이면
    if arr[node][1] in ["-", "+", "*", "/"]:
        # 왼쪽 값 반환
        left = search(arr[node][2])
        # 오른쪽 값 반환
        right = search(arr[node][3])
        # 계산한 값 반환
        return cal(left, right, arr[node][1])
    else:
        return arr[node][1]

for tc in range(1, 11):
    N = int(input())
    # 바로 int, string 분리해서 변환해주기
    arr = [list(map(lambda x: int(x) if x.isdecimal() else x, input().split())) for _ in range(N)]
    # 0번 안쓸거임
    arr = [[0, 0]] + arr

    print(f'#{tc} {int(search(1))}')
