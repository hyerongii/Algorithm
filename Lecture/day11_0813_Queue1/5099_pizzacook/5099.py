import sys
sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())
for tc in range(1, T+1):
    # N 화덕크기 M 피자개수
    N, M = map(int, input().split())
    Q_cheese = list(map(int, input().split()))

    # pizza 번호랑 같이 이동하려면 인덱스랑 같이 묶어주기
    Q_pizza = deque([[i+1, Q_cheese[i]] for i in range(len(Q_cheese))])
    Q_cook = deque()
    # 피자 1번부터 차례로 화덕에 굽기
    for _ in range(N):
        Q_cook.append(Q_pizza.popleft())
    # pizza가 한개 남을때까지
    while len(Q_cook) != 1:
        pass

    '''
    Q 길이 M - 피자 개수
    한번에 N개 구울 수 있음
    1번위치에서 넣거나 뺄 수 있음 [0]에서 하기
    한바퀴 돌때 치즈 양 반으로 줄어듬  
    마지막까지 남아있는 피자 번호?? 번호라서 인덱스 써줘야됨
    7 2 6 5 3     -> 3개 니까 7 2 6 집어 넣음
    7 2 6 -> 1번
    2 6 7
    6 7 2
    7 2 6 이때 한바퀴 완료 -> 7이 절반으로 줄음
    7//2 2 6 
    1 6 7//2 
    3 7//2 1
    3//2 1 3
    1//2 3 3//2 이때 0이므로 다음 피자 집어 넣기 
    '''
