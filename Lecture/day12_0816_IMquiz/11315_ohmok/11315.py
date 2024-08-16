import sys
sys.stdin = open("input.txt", "r")

# 델타로 풀어보기
# 좌대각선 , 위아래, 우대각선, 좌우
dxy = [[-1, -1], [1, 1], [-1, 0], [1, 0], [-1, 1], [1, -1], [0, -1], [0, 1]]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = "NO"
    for i in range(N):
        for j in range(N):
            # 델타 범위
            for k in range(0, 8, 2):
                # 왼쪽
                lx = dxy[k][0]
                ly = dxy[k][1]
                # 오른쪽
                rx = dxy[k+1][0]
                ry = dxy[k+1][1]
                count = 0
                if arr[i][j] == "o":
                    count += 1
                # 두개씩 살피고 모두 0이면 print
                for p in range(1, 3):
                    if 0 <= i+(lx*p) < N and 0 <= j+(ly*p) < N and arr[i+(lx*p)][j+(ly*p)] == "o":
                        count += 1
                    if 0 <= i+(rx*p) < N and 0 <= j+(ry*p) < N and arr[i+(rx*p)][j+(ry*p)] == "o":
                        count += 1
                    if count == 5:
                        result = "YES"
    print(f'#{tc} {result}')
