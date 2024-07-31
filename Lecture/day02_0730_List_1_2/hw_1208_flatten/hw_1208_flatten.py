import sys
sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    dump = int(input())
    arr = list(map(int, input().split()))

# 내가 생각한 방법. 리스트의 최댓값 최솟값 찾기 -> 덤프횟수만큼 계속 반복

    for _ in range(dump):
        pass
        max_num = arr[0]
        min_num = arr[0]
        for i in range(1, len(arr)):
            if arr[i] >= max_num:
                max_num = arr[i]
            if arr[i] <= min_num:
                min_num = arr[i]

        # 값 1씩 - 하기
        if max_num-min_num <= 1:
            print(f'#{test_case} {max_num-min_num}')
            break
        else:
            continue
    print(f'#{test_case} {max_num-min_num}')