import sys
sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T+1):
    test_num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_list = []
    sum_rightdown = sum_leftdown = 0
    reverse_arr = [[0]*100 for _ in range(100)]

    for i in range(100):
        for j in range(100):
            # 행 리스트 다 더한 값 max_list에 차례로 저장
            max_list.append(sum(arr[i]))
            # 대각선 처리
            if i == j :
                sum_rightdown += arr[i][j]
            if 100-i == j :
                sum_leftdown += arr[i][j]
            # 행과 열 바꿔주기
            reverse_arr[i][j] = arr[j][i]

    for i in range(100):
        for j in range(100):
            max_list.append(sum(reverse_arr[i]))

    max_list.append(sum_rightdown)
    max_list.append(sum_leftdown)

    print(f'#{test_case} {max(max_list)}')

'''
- 다른 방법
n=100

for t in range(1,11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    sum_arr = []
    c, d=[], []
    for i in range(n):
        a, b=[], []
        c.append(arr[i][i])
        d.append(arr[n-i-1][i])
        for j in range(n):
            a.append(arr[i][j])
            b.append(arr[j][i])
        sum_arr.extend([sum(a), sum(b)])
    sum_arr.extend([sum(c), sum(d)])
    print(f'#{T} {max(sum_arr)}')
'''

