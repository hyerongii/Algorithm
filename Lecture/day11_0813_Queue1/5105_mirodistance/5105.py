import sys
sys.stdin = open("input.txt", "r")
from collections import deque

def find_start():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j

def bfs():
    queue = deque()
    queue.append((s_x, s_y))
    visited = [[0]*N for _ in range(N)]
    visited[s_x][s_y] = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx = dx+x
            ny = dy+y
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            if visited[nx][ny]: continue
            if arr[nx][ny] == 1: continue
            if arr[nx][ny] == 3:
                return visited[x][y]-1
            queue.append((nx, ny))
            visited[nx][ny] = visited[x][y]+1
    return 0

# 델타 하,우,상,좌
dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    # 시작점 찾기 2가 어디에나 있을 수 있음;;
    s_x, s_y = find_start()
    result = bfs()
    print(f'#{tc} {result}')
