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
        # 각 행의 길이 저장하는 리스트 만들어주기
        row_len_lst.append(len(row))
        # 총 arr 만들어주기
        arr.append(row)

    # 제일 긴 행의 길이로 열마다 원소들 묶어 주는 리스트 만들기
    max_col = max(row_len_lst)
    lst = [[] for _ in range(max_col)]

    # 각 행의 길이 까지 돌면서 각 열의 원소들 하나로 묶어 주기
    for i in range(N):
        for j in range(row_len_lst[i]):
            lst[j].append(arr[i][j])

    min_v = 10000
    max_v = 0
    # 범위 구간 지정 못하면 -1
    result = -1

    # 길이가 M 이상일 때 M만큼 슬라이싱 하면서 합 구하고 최대 최소 찾기
    for i in range(max_col):
        Q = len(lst[i])
        sum_v = 0
        if Q >= M:
            for j in range(Q-M+1):
                sum_v = sum(lst[i][j:j+M])
                if max_v < sum_v:
                    max_v = sum_v
                if min_v > sum_v:
                    min_v = sum_v
            result = max_v - min_v

    print(f'#{tc} {result}')

