import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = []
    cnt = 1
    for _ in range(N):
        current, back = map(int, input().split())
        if rooms:
            for c, b in rooms:
                if (current < b and back > c) or (current > b and back < c):
                    cnt += 1
        rooms.append((current, back))
    print(f'#{tc} {cnt}')