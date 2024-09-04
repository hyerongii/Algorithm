import sys
sys.stdin = open('input.txt')

# 배열 최소합 문제랑 거의 비슷.. 사실 배열 최대합일듯
def dfs(n, sum_v):
    global max_v

    # 백트래킹 해주기 합한게 맥스 값보다 작으면 굳이 할 필요 없음
    if max_v >= sum_v:
        return

    # dfs 종료조건. visited 마지막에 도착하면 결과값과 sum_v 중에 큰거 리턴
    if n == N:
        max_v = max(max_v, sum_v)
        return

    # 열 탐색 한다고 생각하면 됨
    for i in range(N):
        # 방문한 행 표시하기
        if not visited[i]:
            visited[i] = 1
            dfs(n+1, sum_v*arr[n][i]/100)
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    # 직원:일 1:1
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0           # 최댓값 구하기
    visited = [0] * N   # 방문한 열 체크
    dfs(0, 1)

    print(f'#{tc} {max_v*100:.06f}')
