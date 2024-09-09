import sys
sys.stdin = open("input.txt", "r")

T = int(input())
result_lst = []
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())

    # 리스트에 값으로 표시 하니까 에러남...
    # 간단계산 로직도 에러남...
    # 테케 5만개, 출력이 많은 경우 몰아서 하자 (buffer 개념)

    start = max(A, C)
    end = min(B, D)

    answer = end - start
    if answer < 0:
        answer = 0

    result_lst.append(answer)

for index, result in enumerate(result_lst):
    print(f'#{index+1} {result}')