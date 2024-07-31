T = 10
for test_case in range(1, T+1):
    test_num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_list = []
    for i in range(100):
        for j in range(100):
            max_list.append(sum(arr[i]))

    print(f'#{test_case} {max(max_list)}')

