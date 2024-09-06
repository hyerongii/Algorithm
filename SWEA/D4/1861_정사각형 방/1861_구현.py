import sys
sys.stdin = open('input.txt')

'''
1차원 리스트 만들어서 연속(+1)하면 그 인덱스에 1추가 그리고 max값 갱신
arr = [0]*(N**2+1)
'''
dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0]*(N**2+1)

    # arr 탐색하면서 연속하면 1 표시하기
    for i in range(N):
        for j in range(N):
            for dx, dy in dxy:
                nx = i + dx
                ny = j + dy
                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue
                if arr[nx][ny] == arr[i][j] + 1:
                    visited[arr[i][j]] = 1
                    break
    # 그리고 visited 리스트 확인해서 1인거 더해주기 0이면 초기화
    cnt = 0
    max_c = 0
    start = 0
    for i in range(N**2-1, -1, -1):   # 뒤에서 부터 봐주기
        if visited[i]:
            cnt += 1
        else:
            # 다 더해준거에서 작은거 고르기
            if max_c <= cnt:
                max_c = cnt
                start = i + 1
            cnt = 0

    print(f'#{tc} {start} {max_c+1}')
