def finding_location():
    # 처음 위치
    current = 0
    # 만약 K 이동했을때 먹이가 있다면
    while arr[current]:
        # K만큼 계속 이동
        current += K
        # 탈출조건 마지막에 도착했을때
        if current >= N-1:
            return N
    # 없다면 그 위치 반환
    return current+1

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result = finding_location()
    print(f'#{tc} {result}')
