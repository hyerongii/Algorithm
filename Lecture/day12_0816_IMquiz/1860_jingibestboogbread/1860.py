# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    # N:사람 수 M:걸리는 시간(초) K: 붕어빵 수
    N, M, K = map(int, input().split())
    # 사람 방문 시간 리스트
    customer_lst = list(map(int, input().split()))
    # 사람들 중에서 가장 방문 시간 늦은 것 기준으로 돌리기
    # 시간을 인덱스로 고려하기
    customer_lst.sort()
    max_c = customer_lst[-1]
    boongs = [0] * (max_c+1)
    for time in range(1, max_c+1):
        # M초 마다 K개 만큼 생성 쭉 이어져 가야해서 몫으로 생각해주기
        boongs[time] += K*(time//M)
    result = "Possible"
    for customer in customer_lst:
        if boongs[customer] >= 1:
            for boong in range(customer, max_c+1):
                boongs[boong] -= 1
        else:
            result = "Impossible"
            break
    print(f'#{tc} {result}')

