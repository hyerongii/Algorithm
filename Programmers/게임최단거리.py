from collections import deque
def solution(maps):
    # 캐릭터는 항상 1,1 위치에 있음
    # 상대방은 항상 n,m 위치에 있음 point!!

    # maps로 n, m 알아내기 확인
    n = len(maps)
    m = len(maps[0])

    # bfs로 델타 돌려서 최소 거리 찾기
    dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    start = [0, 0]
    visited = [[-1]*m for _ in range(n)]

    q = deque()
    q.append(start)
    visited[0][0] += 1

    while q:
        x, y = q.popleft()

        if x == m-1 and y == n-1:
            break

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            if 0 > nx or nx >= n or 0 > ny or ny >= m or visited[nx][ny] > -1 or maps[nx][ny] == 0: continue
            visited[nx][ny] = visited[x][y] + 1
            q.append([nx, ny])

    answer = visited[n-1][m-1]

    # 도착 거리도 포함해야해서 +1 해주기
    if answer > -1:
        answer += 1

    return answer

