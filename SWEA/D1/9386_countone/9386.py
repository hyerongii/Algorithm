import sys
sys.stdin = open("input.txt", "r")

def count_one():
    max_count = 1
    count = 1
    for i in range(N-1):
        if arr[i] == 1 and arr[i+1] == 1:
            count += 1
        elif arr[i] == 1 and arr[i+1] == 0:
            count = 1
        if max_count < count:
            max_count = count
    return max_count

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    print(f'#{tc} {count_one()}')