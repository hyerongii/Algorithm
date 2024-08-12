import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    grassland = list(input())

    count = 0

    # 공이 있을 경우는 (|, |), () 이 3가지
    for i in range(len(grassland)-1):
        if grassland[i] == "(" and grassland[i+1] == ")":
            count += 1

        elif grassland[i] == "(" and grassland[i+1] == "|":
            count += 1

        elif grassland[i] == "|" and grassland[i+1] == ")":
            count += 1

    print(f'#{tc} {count}')
