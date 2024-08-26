def dfs(i, n, sum_v):
    global sum_tmp

    # 최대값보다 크면 반환
    if sum_tmp < sum_v: return

    # dfs 종료조건. 마지막 열 도착했을 때 작은 값 리턴
    if n == N:
        sum_tmp = min(sum_tmp, sum_v)
        return

    for j in range(N):
        if n != j and not visited[j]:
            visited[j] = True
            dfs(i, j, sum_v+arr[n][j])
            visited[j] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # dfs 백트레킹 문제 n-queen에서 조건 더 있음;;
    # 방문한 열 있을 경우 표시
    visited = [False]*N
    # 나올 수 있는 최대 값 (6400)
    sum_tmp = 1000
    # 처음 행 위치, 위험도합
    for i in range(N):
        dfs(i, 0, 0)
    print(f'#{tc} {sum_tmp}')