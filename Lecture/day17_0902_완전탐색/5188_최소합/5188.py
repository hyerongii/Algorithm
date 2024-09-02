import sys
sys.stdin = open("input.txt", "r")

# DFS BFS 둘 다 풀어보기
# 델타탐색
dxy = [[0, 1], [1, 0]]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 1,0 ~ N-1,N-1 까지 조사
    # visited 에 지나온 경로의 합 넣어주기
