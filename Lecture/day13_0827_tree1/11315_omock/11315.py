import sys
sys.stdin = open("input.txt", "r")

# 위아래 0 1/ 좌우 2 3/ 좌대각선 4 5/ 우대각선 6 7
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [1, 1], [-1, 1], [1, -1]]

def omok():
    for i in range(N):
        for j in range(N):
            for k in range(len(dxy) // 2):  # 0 1 2 3
                count = 0
                for l in range(1, 3):
                    nx = dxy[2 * k][0] * l
                    ny = dxy[2 * k][1] * l

                    if arr[i][j] != "o": continue
                    if 0 > nx or nx >= N or 0 > ny or ny >= N: continue
                    if arr[nx][ny] == "o":
                        count += 1
    if count == 4:
        return "YES"
    else:
        return "NO"


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    # 두개씩 비교하깅 dx*2k dy*2k
    result = omok()
    print(f'#{tc} {result}')



