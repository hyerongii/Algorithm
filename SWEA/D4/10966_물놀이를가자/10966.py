import sys
sys.stdin = open('input.txt')
from collections import deque

dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def bfs(N, M):
    ans = 0
    q = deque()

    # 거리 visited에 저장해줄거임
    visited = [[-1] * M for _ in range(N)]

    # 출발점 인큐 (모든 물 W의 인덱스 찾기)
    # 출발점 인큐 표시
    for i in range(N):
        for j in range(M):
            if arr[i][j] == "W":
                q.append((i, j))
                visited[i][j] = 0   # 방문했다표시하기

    while q:
        i, j = q.popleft()
        for dx, dy in dxy:
            nx, ny = i + dx, j + dy
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                q.append((nx, ny))
                visited[nx][ny] = visited[i][j] + 1
                ans += visited[nx][ny]
    return ans

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    ans = bfs(N, M)        # 모든 땅에서 물까지의 최단거리
    print(f'#{tc} {ans}')
    # 거리니까 물(도착지) 기준으로 생각해도 된다.
