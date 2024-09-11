import sys
sys.stdin = open('input.txt')

dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

'''
이거는 dfs로 풀어보자!
'''

def dfs(x, y):
    global cnt

    # 시작점 좌표에서 방을 이동하는 경우 돌리기
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if arr[nx][ny] == arr[x][y] + 1:
            cnt += 1
            dfs(nx, ny)
            break

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_c = 0
    max_room = 1001
    # 중요한건 시작좌표, 이동한 카운트
    for i in range(N):
        for j in range(N):
            cnt = 0
            dfs(i, j)
            if max_c < cnt:
                max_c = cnt
                # 그 시작좌표의 값 저장하기
                max_room = arr[i][j]
                # 만약 최대인 방 여러개라면
            elif max_c == cnt:
                if max_room > arr[i][j]:
                    max_room = arr[i][j]

    print(f'#{tc} {max_room} {max_c+1}')

# 쌤방법

# dy = [-1, 0, 1, 0]
# dx = [0, -1, 0, 1]
#
# def DFS(sy, sx):
#     global board, cnt
#     for i in range(4):
#         ny, nx = sy + dy[i], sx + dx[i]
#         if 0 <= ny < N and 0 <= nx < N:
#             if board[ny][nx] == board[sy][sx] + 1:
#                 cnt += 1
#                 DFS(ny, nx)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     max_cnt, resulty, resultx = 0, 0, 0
#     for y in range(N):
#         for x in range(N):
#             cnt = 1
#             DFS(y, x)
#             if max_cnt < cnt:
#                 max_cnt = cnt
#                 resulty = y
#                 resultx = x
#             elif max_cnt == cnt and board[y][x] < board[resulty][resultx]:
#                 resulty = y
#                 resultx = x
#
#     print(f'#{tc} {board[resulty][resultx]} {max_cnt}')
