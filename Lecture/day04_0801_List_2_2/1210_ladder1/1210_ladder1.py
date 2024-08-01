import sys
sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T+1):
    tc = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 배열 끝에 2 값이 최종 도착지
    # 올라가면서 찾는다!!

    di = [-1,0,0]
    dj = [0,-1,1]

    # 이동방향 결정하는 인덱스
    idx = 0         # 0 : 위로 /  1 : 왼쪽으로  / 2 : 오른쪽으로 

    # 주변탐색
    ei = [-1, 0, 0, 1]
    ej = [0, -1, 1, 0]

    # zero padding 하기.. 0으로 다 막아주기
    real_arr = [[0] * 102 for _ in range(102)]  # 0~101 102개
    for i in range(100):
        for j in range(100):
            real_arr[i+1][j+1] = arr[i][j]

    # 출발점 찾기, 출발점에서 시작하기 start point : sp
    sp_i = 100
    sp_j = real_arr[100].index(2)

    while sp_i != 0:
        for e in range(4):
            if real_arr[sp_i+ei[e]][sp_j+ej[e]] == 1:
                if e < 3:
                    sp_i += di[e]
                    sp_j += dj[e]
    
    print(sp_j)



