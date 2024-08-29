import sys
from collections import deque
sys.stdin = open('input.txt')

dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# 1,1 부터 목적지 까지 갈 수 있는지 bfs 사용
def bfs(arr,n):
    queue = deque()
    queue.append((1, 1))
    visited = [[False]*n for _ in range(n)]
    visited[1][1] = True

    while queue:
        x, y = queue.popleft() # 좌표 탐색
        if arr[x][y] == 3: # 만약 도착지에 도착했다면..
            return 1
        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            if 0 > nx or 0 > ny or nx >= n or ny >= n: continue
            if arr[nx][ny] == 1:continue
            if visited[nx][ny]: continue
            queue.append((nx,ny))
            visited[nx][ny] = True
    return 0

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, list(input()))) for _ in range(100)]
    N = 100
    result = bfs(arr, N)
    print(f'#{tc} {result}')
