T = 10
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    empty_house = 0
    for i in range(2, N - 2, 1):

        if (arr[i - 1] < arr[i]) and (arr[i - 2] < arr[i]) and (arr[i + 1] < arr[i]) and (arr[i + 2] < arr[i]):
            num_list = [arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2]]

            max_num = num_list[0]
            for j in range(1, len(num_list)):  # index 0 은 초깃값으로 이미 설정했으니까 1부터
                if max_num < num_list[j]:
                    max_num = num_list[j]

            empty_house += (arr[i] - max_num)

    print(f'#{test_case} {empty_house}')