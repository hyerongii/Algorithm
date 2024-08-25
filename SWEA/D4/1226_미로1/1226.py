import sys
from collections import deque
sys.stdin = open('input.txt')


def is_possible_to_goal(arr, n):
    # 델타탐색 : 하,우,상,좌
    dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    # 시작점 1,1
    # 도착지점 13,13
    queue = deque()
    queue.append((1,1))

    # 방문리스트 만들어주기
    visited = [[False]*n for _ in range(n)]
    # 출발지점 방문 했으니까 바꿔주고 시작
    visited[1][1] = True

    while queue:
        # 이동하는 좌표
        x, y = queue.popleft()
        if x == 13 and y == 13:
            return 1

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            # 델타 범위 검사
            if 0 > nx or nx >= n or 0 > ny or ny >= n: continue
            # 벽인지 확인
            if arr[nx][ny] == 1: continue
            # 방문했던 적이 있는 지 확인
            if visited[nx][ny]: continue
            # 위에 다 통과했으면, 큐에 집어넣고,
            queue.append((nx, ny))
            # 방문했다고 표시
            visited[nx][ny] = True

    return 0

for _ in range(1, 11):
    tc = int(input())
    N = 16
    arr = [list(map(int, list(input()))) for _ in range(N)]

    # BFS를 이용해서 목표지점에 도착하는지 확인
    # 시작지점은 1,1 도착지점은 13,13 항상 고정되어있음;;
    result = is_possible_to_goal(arr, N)
    print(f'#{tc} {result}')
