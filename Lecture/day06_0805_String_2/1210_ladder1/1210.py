import sys
sys.stdin = open("input.txt", "r")

#위좌우
dxy = [[-1, 0], [0, -1], [0, 1]]

# zero-padding이 아닌 다른 방법
def search_ladder(x, y):

    arr[x][y] = 0

    while x != 0:  
        for dx, dy in dxy :
            nx = x + dx
            ny = y + dy

            if 0 <= nx < 100 and 0 <= ny < 100 and arr[nx][ny]:
                arr[x][y] = 0
                x, y = nx, ny
    return y

T = 10
for test_case in range(1, T+1):
    tc = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    for j in range(100):
        if arr[99][j] == 2:
            result = search_ladder(99,j)

    print(f'#{test_case} {result}')