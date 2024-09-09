import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    # 3개씩 들어옴..
    A, B, C = map(int, input().split())
    cnt = 0
    if C <= B:
        while C <= B:
            B -= 1
            cnt += 1
    if B <= A:
        while B <= A:
            A -= 1
            cnt += 1
    if A < 1 or B < 1 or C < 1:
        cnt = -1
    print(f'#{tc} {cnt}')




