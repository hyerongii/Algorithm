'''
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
'''

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    maximum = arr[0]  # 초깃 값은 배열의 첫 번째 값으로 설정
    for i in range(1, N):  # index 0 은 초깃값으로 이미 설정했으니까 1부터
        if maximum < arr[i]:
            maximum = arr[i]

    minimum = arr[0]
    for i in range(1, N):
        if minimum > arr[i]:
            minimum = arr[i]

    answer = maximum - minimum
    print(maximum, minimum)
    print(f'#{test_case} {answer}')