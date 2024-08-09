import sys
sys.stdin = open("input.txt", "r")

# 확인한 값 개수, 현재 위치, 현재 더한 값
def finding_small_sum(depth, ci, cj, c_sum):
    # 행렬 돌면서 선택한 값 중에서 arr[i][:] 금지 arr[:][j] 금지
    # 값의 위치 저장해서 계속 안되는 조건 부여해주기
    for i in range(N):
        for j in range(N):

            # 모든 수 다 반복하면
            if depth == N*N:
                return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    depth = 0
    c_sum = 0

    for i in range(N):
        for j in range(N):
            finding_small_sum(depth, i, j, c_sum)


