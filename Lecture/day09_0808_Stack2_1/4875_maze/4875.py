def fstart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input().split())) for _ in range(N)]

    # 출발위치 찾기
    sti, stj = fstart(N)