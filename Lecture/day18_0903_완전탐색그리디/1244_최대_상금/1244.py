import sys
sys.stdin = open('input.txt')

def search(lev):
    global max_n

    if lev == N:
        result = int("".join(num))
        if result > max_n:
            max_n = result
        return

    for i in range(len(num)):
        for j in range(i+1, len(num)):

            num[i], num[j] = num[j], num[i]

            if (lev, "".join(num)) not in visited:
                visited.add((lev, "".join(num)))
                search(lev + 1)

            num[j], num[i] = num[i], num[j]

T = int(input())
for tc in range(1, T+1):
    num, N = map(int, input().split())
    num = list(str(num))
    max_n = 0
    visited = set()
    search(0)

    print(f'#{tc} {max_n}')
