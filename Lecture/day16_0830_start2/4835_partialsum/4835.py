import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 이웃한 M개의 합이기 때문에 M만큼 슬라이싱해서 합 구하고 최소 최대 각각 찾기
    max_v, min_v = 0, sum(arr[:M])
    for i in range(N-M+1):
        sum_v = sum(arr[i:i+M])
        if sum_v > max_v:
            max_v = sum_v
        if sum_v < min_v:
            min_v = sum_v

    print(f'#{tc} {max_v-min_v}')
