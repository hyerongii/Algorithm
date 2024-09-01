T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(input())

    # 가장 긴 데칼코마니의 길이 알아내는 프로그램
    # 기준점 기준으로 왼쪽 오른쪽 값 비교 근데 점차 늘려가는..
    max_v = 1
    for i in range(1, N//2+1): # 1234
        cnt = 1
        for j in range(1, i+1): # 1
            if arr[i+j] == arr[i-j]:
                max_v = cnt + j*2
            else:
                break
        # if max_v < cnt:
        #     max_v = cnt

    print(f'#{tc} {max_v}')

'''
    3
    3
    100
    5
    10101
    10
    1011011110
    
'''

