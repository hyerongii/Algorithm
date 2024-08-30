import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    # 행의 길이 저장하는 리스트 만들기
    row_len_lst = []
    for _ in range(N):
        row = list(map(int, input().split()))
        row_len_lst.append(len(row))
        arr.append(row)

    min_v = 10000
    max_v = 0
    for i in range(N):
        for j in range(N-M+1):
            # 연속 M 개수 슬라이싱
            sum_v = 0
            if row_len_lst[i] >= M:
                for k in range(M):
                    sum_v += arr[j+k][i]
            if max_v < sum_v:
                max_v = sum_v
            if min_v > sum_v:
                min_v = sum_v

    print(max_v, min_v)

