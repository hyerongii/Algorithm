import sys
sys.stdin = open("input.txt", "r")

dxy = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
balls = [0, 2, 1]  # 1-> 넣었을때 2->넣었을때

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # NxN의 오목판 만들기 1: 흑돌 2: 백돌
    arr = [[0]*N for _ in range(N)]
    # (4,4) (6,6) (8,8) 일 때 다 일정한 위치에 해주려면
    arr[N//2-1][N//2-1] = 2
    arr[N//2-1][N//2] = 1
    arr[N//2][N//2-1] = 1
    arr[N//2][N//2] = 2
    # M번 반복
    for _ in range(M):
        # 받은 위치, 공의 색 대입
        y, x, input_ball = map(int, input().split())
        arr[x-1][y-1] = input_ball
        # 만약 나의 좌표 사이에 상대편 돌 있을때,,
        for dx, dy in dxy:
            nx = dx+(x-1)
            ny = dy+(y-1)
            temp = []
            # 주변에 자기와 다른 색이 있으면
            while 0 <= nx+dx < N and 0 <= ny+dy < N and arr[nx][ny] == balls[input_ball]:
                # 뒤집을 돌 저장하고 계속이동...!! keypoint
                temp.append((nx, ny))
                nx, ny = dx + nx, dy + ny
                # 그 위치에서 같은 델타에서의 색 확인 또 돌리자
                if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == input_ball:
                    for (p, q) in temp:
                        arr[p][q] = input_ball
    count_W = 0
    count_B = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                count_B += 1
            elif arr[i][j] == 2:
                count_W += 1
    print(f'#{tc} {count_B} {count_W}')





