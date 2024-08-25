import sys
sys.stdin = open("input.txt", "r")

# K 만큼 이동할 수 있음 그때 충전기 찾기
# 충전기 없으면 그 전 충전기 있는 곳으로 가서 충전하고 카운트
# 다시 이동 반복

# busstop K배수 만큼 돌기 chargestop 아니면 돌아가서 찾기
# 돌아가서 또 K배수 만큼 이동하려면 변수 값 계속 바뀌어야해서 while문 사용

def count_charge():
    stop = 0
    while True:
        stop += K
        if stop >= N:
            return sum(bus_stop)
        tmp = stop
        while stop not in charge_stop:
            stop -= 1
            if stop == tmp-K:
                return 0
        bus_stop[stop] += 1


T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_stop = list(map(int, input().split()))
    # 0~N 버스정류장, 충전하면 그 정류장의 인덱스에 수 할당하기 위해서
    bus_stop = [0]*(N+1)
    print(f'#{tc} {count_charge()}')




