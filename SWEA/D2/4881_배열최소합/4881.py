import sys
sys.stdin = open("input.txt", "r")

def dfs(n, sum_v):
    global result
    # 결과가 sum_v보다 작으면 그값 return
    if result <= sum_v:
        return
    # dfs 종료조건. 마지막 열 도착했을때 결과값이랑 sum_v중에 작은값 리턴
    if n == N:
        result = min(result, sum_v)
        return
    #  방문한 행은 표시하기
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(n+1, sum_v + arr[n][i])
            # 한바퀴 다 돌고 나서 합 구하고 다시 두번째 행부터 보려면,,
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 열 방문했는지 체크해주기 위해서 만듬
    visited = [0] * N
    # 최댓값 집어넣어줘서 제일 작은 값 뽑아내기
    result = 100
    dfs(0, 0)

    print(f'#{tc} {result}')


