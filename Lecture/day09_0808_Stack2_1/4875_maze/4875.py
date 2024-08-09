import sys
sys.stdin = open("input.txt", "r")

# 출발지점 좌표 찾기
def fstart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

dxy = [[-1,0],[0,1],[1,0],[0,-1]]

def moving_to_definition(cti, ctj): # 현재위치 넘기기

    if maze[cti][ctj] == 3: # 목적지에 도착하면
        global result
        result = 1
        return

    # 방문한곳 true로 바꾸기
    visited[cti][ctj] = True

    for k in range(len(dxy)):
        dx, dy = dxy[k]
        nx, ny = cti+dx, ctj+dy
        if 0 > nx or 0 > ny or N <= nx or N <= ny:
            continue
        if maze[nx][ny] != 1 and not visited[nx][ny]:
            moving_to_definition(nx, ny)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]

    # 출발위치 찾기
    sti, stj = fstart(N)

    visited = [[False]*N for _ in range(N)]
    result = 0

    # 현재위치 = 시작위치 (처음)
    moving_to_definition(sti, stj)

    print(f'#{tc} {result}')



