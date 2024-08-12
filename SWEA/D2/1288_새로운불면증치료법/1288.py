import sys
sys.stdin = open("input.txt", "r")

# 0~9 까지 숫자 리스트 생성
num_lst = list(map(str, range(10)))

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 0~9를 index로 가지는거 카운트하는 리스트
    count_lst = [0] * 10
    i = 1

    # N의 배수만큼 반복해서 num_lst에 해당하면 그 인덱스를 가지는 카운트리스트 체크
    while True:
        num = N*i

        # str으로 변환해서 리스트 만들어서 확인하는 방법 사용했지만, 나머지를 비교하는 방법도 있을 듯
        str_num_lst = list(str(num))

        for c in str_num_lst:
            if c in num_lst:
                count_lst[int(c)] += 1

        if 0 not in count_lst:
            print(f'#{tc} {num}')
            break

        i += 1