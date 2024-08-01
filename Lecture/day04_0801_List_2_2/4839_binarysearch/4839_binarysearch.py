import sys
sys.stdin = open("input.txt", "r")

def binarySearch(arr, N, key):
    start = 0     # 시작원소 인덱스
    end = N-1   # 마지막원소 인덱스
    count = 0
    while start <= end:
        count += 1
        middle = (start + end)//2
        if arr[middle] == key: # 검색성공
            return count
        elif arr[middle] > key:
            end = middle # 왼쪽 값만 살리기
        else: 
            start = middle # 오른쪽 값만 살리기

T = int(input())
for test_case in range(1, T+1):
    # 전체 페이지 수: P, 찾을 페이지 수 A, B
    P, A, B = map(int, input().split()) 
    arr = list(range(1, P+1))

    countA = binarySearch(arr, P, A)
    countB = binarySearch(arr, P, B)

    if countA > countB:
        print(f'#{test_case} B')
    elif countA == countB:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} A')