import sys
sys.stdin = open('input.txt')

# N이 100개라서 재귀 가능... n00이면 재귀는 가급적 사용 자제

def f(i, N):
    visited[i] = 1
    for j in adjL[i]:   # i와 아는 관계인 j가 속한 무리가 없으면
        if visited[j] == 0:
            f(j, N)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    visited = [0] * (N+1)       # 관계가 확인된 사람

    adjL = [[] for _ in range(N + 1)]       # 인접리스트 만들기
    for i in range(M):
        x, y = map(int, input().split())
        adjL[x].append(y)  # 방향 두 방향 이면 두개 추가
        adjL[y].append(x)

    cnt = 0                     # 무리의 수
    for i in range(1, N+1):
        if visited[i] == 0:
            cnt += 1
            f(i, N)

    print(f'#{tc} {cnt}')