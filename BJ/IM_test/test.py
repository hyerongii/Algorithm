import sys
sys.stdin = open('input.txt')

# 스위치 개수
switch_num = int(input())
# 스위치의 상태
arr = list(map(int, input().split()))
# 학생 수
person_num = int(input())
# 스위치 -> 0이랑 1밖에 없음
switch = {0:1, 1:0}

for _ in range(person_num):
    gender, num = map(int, input().split())

    # 성별 구분해서 처리해주기
    # 남자면
    if gender == 1:
        # 스위치의 개수 안에서 받은 숫자의 배수의 스위치를 변환
        for i in range(1, switch_num+1):
            if i % num == 0:
                arr[i-1] = switch[arr[i-1]]
    # 여자면
    elif gender == 2:
        # 좌우가 대칭이면서 가장 많은 스위치 포함하는 구간 찾기
        # 간이 델타,,?  num-1 에서 부터 좌우로 찾기
        # 범위 스위치 개수 - 숫자 숫자 - 1 중에 작은거까지만 찾기
        ran_sw = min(switch_num-num, num-1)
        # 중간꺼 처음에 바꿔버려...
        arr[num - 1] = switch[arr[num - 1]]
        for i in range(1, ran_sw+1):
            if arr[num-1-i] == arr[num-1+i]:
                arr[num-1-i] = switch[arr[num-1-i]]
                arr[num-1+i] = switch[arr[num-1+i]]
            else:
                break

for i in range(len(arr)):
    if i % 20 == 19:
        print(arr[i], end=" ")
        print()
    else:
        print(arr[i], end=" ")