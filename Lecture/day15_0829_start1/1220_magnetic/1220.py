import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    stack = []
    count = 0
    # 1,2 이 구조로 나와야함
    # 열 우선 탐색으로 가야됨
    for i in range(N):
        stack = []
        for j in range(N):
            # arr[j][i] == 1 이면 stack에 저장 그다음에 2 나오면 카운트 해주기
            if arr[j][i] == 1:
                stack.append(1)
            if stack and stack[-1] == 1 and arr[j][i] == 2:
                count += 1
                stack = []

    print(f'#{tc} {count}')
