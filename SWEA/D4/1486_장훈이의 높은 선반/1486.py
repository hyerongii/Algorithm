import sys
sys.stdin = open('input.txt')

'''
부분집합, dfs, visited 필요없음 -> 트리같이생각
'''

def search(cnt, sum_v):
    # 간격 제일 작은거
    global min_v

    if sum_v >= B:
        min_v = min(min_v, sum_v)
        return

    if cnt == N:
        return

    search(cnt+1, sum_v+arr[cnt])
    search(cnt+1, sum_v)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    # 완탐, 가지치기
    min_v = 200000
    search(0, 0)

    print(f'#{tc} {min_v-B}')
