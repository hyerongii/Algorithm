import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    # 버스노선
    N = int(input())
    buses = []
    # 방문한거 확인해서 카운트하는 리스트
    visited = []
    for _ in range(N):
        # 몇번 버스 인지 리스트에 추가
        N_bus = list(map(int, input().split()))
        buses.append(N_bus)
    # 버스정류장 개수
    P = int(input())
    # 버스정류장 입력받으면서 n번 버스가 지나는지 확인
    for _ in range(P):
        bus_stop = int(input())
        count = 0
        for n_bus in buses:
            for bus in range(n_bus[0], n_bus[1]+1):
                if bus == bus_stop:
                    count += 1
        visited.append(count)

    print(f'#{tc}', end=" ")
    print(*visited)


