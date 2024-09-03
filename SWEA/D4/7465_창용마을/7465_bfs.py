import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(i):
    queue = deque()
    queue.append(i)
    visited[i] = 1    # bfs 준비 과정

    while queue:
        i = queue.popleft()
        for j in adjL[i]:                       # 인접 정점이 방문 전이면 꺼내서 확인하기
            if not visited[j]:                  # 방문 안했으면..
                queue.append(j)                 # 인큐하고
                visited[j] = visited[i]+1       # 방문 확인하기 방문에 길이 같이 저장하기

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    visited = [0] * (N+1)       # 관계가 확인된 사람

    adjL = [[] for _ in range(N + 1)]       # 인접리스트 만들기
    for i in range(M):
        x, y = map(int, input().split())
        # 만약 문제에 중복된 관계가 있다고 하면 set 써주기
        adjL[x].append(y)  # 방향 두 방향 이면 두개 추가
        adjL[y].append(x)

    cnt = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            cnt += 1
            bfs(i)

    print(f'#{tc} {cnt}')