import sys
sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())
for tc in range(1, T+1):
    # N 화덕크기 M 피자개수
    N, M = map(int, input().split())
    Q_cheese = deque(map(int, input().split()))

    # pizza 번호랑 같이 이동하려면 인덱스랑 같이 묶어주기
    Q_pizza = deque([[i+1, Q_cheese[i]] for i in range(len(Q_cheese))])
    Q_cook = deque()
    # 피자 1번부터 차례로 화덕에 먼저 넣기
    for _ in range(N):
        Q_cook.append(Q_pizza.popleft())  # 726 5,3 은 남아있음
    # pizza가 한개 남을때까지
    while len(Q_cook) != 1:
        for _ in range(N):
            if len(Q_cook) == 1:
                break
            # 돌때마다 반씩 줄고 뒤쪽에 넣어주기
            Q_cook[0][1] //= 2
            Q_cook.append(Q_cook[0])
            # 만약 치즈양 0이면 내보내고 새피자 넣기
            if Q_cook[0][1] == 0:
                Q_cook.popleft()
                Q_cook.pop()
                if Q_pizza:
                    Q_cook.append(Q_pizza.popleft())
            else:
                Q_cook.popleft()

    print(f'#{tc} {Q_cook[0][0]}')

