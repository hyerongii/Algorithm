import sys
sys.stdin = open("input.txt", "r")

# 최소힙 구하는 코드
# 입력 순서대로 최소힙에 저장하기
def enq(n):
    global last
    last += 1       # 마지막 노드 추가
    h[last] = n
    c = last        # 부모 자식 비교를 위해서
    p = c//2
    while p >= 1 and h[p] > h[c]: # 부모 있고, 새로 들어온 값이 작으면
        h[p], h[c] = h[c], h[p] # swap 하기
        c = p
        p = c//2

# 입력 코드
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 우선 최소힙을 저장할 리스트 생성 0번 안쓸거임
    h = [0]*(N+1)
    # 힙의 마지막 노드 번호 - 재귀 돌아갈 때 마다 바뀜
    last = 0

    # arr 원소 하나씩 힙에 넣어주기 - 루트값만 최솟값이라고 볼 수 있음
    for num in arr:
        enq(num)

    # 마지막 노드의 조상 노드에 저장된 정수의 합 구하기
    # h list에서 마지막 index는 노드 개수와 같다 거기서 N//2 돌리면서 0될때까지 합해주기
    idx = N
    sum_v = 0
    while idx != 0:
        idx //= 2
        sum_v += h[idx]

    print(f'#{tc} {sum_v}')