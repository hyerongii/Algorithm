def fstart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i,j

def farrive(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:
                return i,j

dxy = [[-1,0],[0,1],[1,0],[0,-1]]

def moving_to_definition(cti, ctj): # 현재위치 넘기기
    if cti == ari and ctj == arj : # 목적지에 도착하면
        print(f'#{tc} {1}')
        return

    # 방문한곳 true로 바꾸기
    visited[cti][ctj] = True
    
    for i in range(N):
        for j in range(N):
            for k in range(len(dxy)):
                dx, dy = dxy[k]
                nx, ny = i+dx, j+dy

            if maze[i][j] :
                pass

    

# 함수어떻게 구현할건지?
# 현재위치 델타로 돌리면서 주변에 0이 있는지 확인 이동 후에 방문지점 true로 바꾸기

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input().split())) for _ in range(N)]

    # 출발위치 찾기
    sti, stj = fstart(N)

    # 목적지 찾기
    ari, arj = farrive(N)
    
    stack = []
    visited = [[False] for _ in range(N)]

    # 현재위치 = 시작위치 (처음)
    moving_to_definition(sti,stj)


