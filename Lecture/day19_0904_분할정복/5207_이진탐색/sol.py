import sys
sys.stdin = open('input.txt')

# 양쪽 구간 번갈아 선택하게 되는 숫자의 개수 ??
def binary_search(n):
    low = 0
    high = N-1
    # 마지막 내가 움직였던 값 저장
    last_dir = 0  # 왼쪽 -1 , 오른쪽 +1

    while low <= high:
        mid = (low+high)//2
        # 만약 값이 나왔다면 무조건 True 반환
        if A[mid] == n:
            return True
        # 기준점보다 왼쪽일때
        elif A[mid] > n:
            high = mid - 1
            # 마지막 저장된 값이 -1 이면
            if last_dir == -1:
                # 바로 False 리턴
                return False
            # 마지막 값 -1 저장
            last_dir = -1
        # 기준점보다 오른쪽일때 반대로 똑같이 생각
        else:
            low = mid + 1
            if last_dir == 1:
                return False
            last_dir = 1
    # 다 돌았으면 원소 없는거임. False 반환
    return False

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # A 오름차 순으로 정렬
    A.sort()

    answer = 0
    # B에 있는 숫자들 이진검색 돌리기
    for num in B:
        result = binary_search(num)
        # 만약 True 면
        if result:
            # 답 횟수 증가
            answer += 1
    print(f'#{tc} {answer}')



