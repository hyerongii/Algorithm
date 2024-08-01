import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    # 이거 무조건 익숙해지기
    arr = [list(map(int, input().split())) for _ in range(N)]
    r1 = arr[0]
    c1 = arr[1]
    r2 = arr[2]
    c2 = arr[3]
    color = arr[-1]

    blank_arr = [[0]*10 for _ in range(10)]
    
