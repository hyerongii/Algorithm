# import sys
# sys.stdin = open("input.txt", "r")

# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())

T = 1
for test_case in range(1, T+1):
    N = 3

# 꼭짓점 만나면 방향 틀기
# i 그대로 j 증가
# i 증가 j 그대로
# i 그대로 j 감소
# i 감소 j 그대로

    # 먼저 N 크기 배열 만들기
    blank_arr = [[0]*N for _ in range(N)]

    # 0, N 으로 만들 수 있는 꼭짓점
    # num = list(range(1, N+1))

    i = 0
    j = 0
    num = 1

    while j != N:
        blank_arr[i][j] = num
        j += 1
        num += 1
    while i != N:
        blank_arr[i][j] = num
        i += 1
        num += 1
    while j != 0:
        blank_arr[i][j] = num
        j -= 1
        num += 1
    while i != 0:
        blank_arr[i][j] = num
        i -= 1
        num += 1
        
    print(blank_arr)



