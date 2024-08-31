import sys
sys.stdin = open('input.txt')
from collections import deque

for tc in range(1, 11):
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))

    # 인접행렬 만들기
    # 사람 최대 100명 (0번 안쓸거임)
    lst = [[0]*101 for _ in range(101)]
    # x->y 로 진행함
    for i in range(N//2):
        x = arr[2*i]        # 출발지
        y = arr[2*i+1]      # 목적지
        lst[x][y] = 1



    # 출발점 표시
    queue = deque()
    queue.append(start)
    # 방문 표시
    visited = [False]*10
    visited[start] = True

    # 도착점 있을 때 까지 반복
    while queue:
        # 현재 위치
        x = queue.popleft()

        # 목적지가 없으면 멈춤
        if lst[x] == 0: continue
        # 방문한 적 있으면 멈춤
        if visited[x]: continue

        queue.append(lst[x])

