import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input()))

    max_count = 0
    count = 1

    for i in range(len(arr)-1):
        if arr[i] == 1 and arr[i+1] == 1:
            count += 1
        else: count


    print(f'#{tc} {count}')