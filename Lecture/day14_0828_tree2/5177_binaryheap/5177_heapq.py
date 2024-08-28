import sys
sys.stdin = open("input.txt", "r")
from heapq import heappush

# pypy에서 에러나서,, 그냥 함수 써주기

# 입력 코드
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 힙 리스트
    h = []

    # 최소힙 써보기
    for num in arr:
        heappush(h, num)

    h = [0]+h

    # 마지막 노드의 조상 노드에 저장된 정수의 합 구하기
    # h list에서 마지막 index는 노드 개수와 같다 거기서 N//2 돌리면서 0될때까지 합해주기
    idx = N
    sum_v = 0
    while idx != 0:
        idx //= 2
        sum_v += h[idx]

    print(f'#{tc} {sum_v}')