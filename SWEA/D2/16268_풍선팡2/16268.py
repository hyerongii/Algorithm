import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 델타 표기법 확인
    dxy = [[0,0], [0,1], [0,-1], [1,0], [-1,0]]

    max_v = 0

    for i in range(N):
        for j in range(M):
            sum_v = 0
            # 차례로 확실하게 표시
            for dx, dy in dxy:
                nx = i+dx
                ny = j+dy

                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue

                sum_v += arr[nx][ny]
            
            if max_v < sum_v:
                max_v = sum_v

    print(f'#{test_case} {max_v}')



