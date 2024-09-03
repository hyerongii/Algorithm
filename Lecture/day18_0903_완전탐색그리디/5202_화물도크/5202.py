import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 시작, 종료 시간, 걸리는 시간 3개 묶은 리스트 리스트에 저장 - 이중리스트
    time_lst = []
    for _ in range(N):
        s, e = map(int, input().split())
        time_lst.append([s, e])

    # 걸리는 시간이 작은 순서대로(2번 원소 기준으로) 정렬
    time_lst.sort(key=lambda x: x[1])

    cnt = 0
    end = 0
    for time in time_lst:
        # 시작 타임 뒤로 아무도 차지한 적 없는 시간일 때
        if end <= time[0]:
            end = time[1]
            cnt+=1

    print(f'#{tc} {cnt}')