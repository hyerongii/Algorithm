import sys
sys.stdin = open("input.txt", "r")

from collections import deque

def findingpw(Q_num):
# 감소후 뒤로 이동한 숫자가 0보다 작아질 때 루프 멈춤
    while True:
        # 루프는 5번 반복, 첫번째 1감소 다섯번째 5감소
        for i in range(1,6):
            # 감소시키고
            Q_num[0] -= i
            # 맨뒤로 이동
            Q_num.append(Q_num[0])
            Q_num.popleft()

            if Q_num[-1] <= 0:
                # Q_num에 있는 숫자가 암호가 된다
                Q_num[-1] = 0
                return Q_num

for _ in range(10):
    tc = input()
    Q_num = deque(map(int, input().split()))
    findingpw(Q_num)
    print("#"+tc, *Q_num)
