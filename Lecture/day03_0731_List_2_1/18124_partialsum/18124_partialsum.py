import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = 10
    arr = list(map(int, input().split())) 
    
    zero_exist = 0
    sum_list = []
    # 모든 부분집합 생성!!
    # 원소가 10인 모든 부분집합의 수
    for i in range(1, 1 << 10):
        part_list = []
        # 원소 수 만큼 비트를 비교
        for j in range(N):
            # i의 j번 비트가 1인 경우
            if i & (1 << j):
                part_list.append(arr[j]) # 부분집합 리스트로 만들기
        sum_list.append(part_list)
    
    for s in sum_list:
        if sum(s) == 0:
            zero_exist = 1
            break
    
    print(f'#{test_case} {zero_exist}')
