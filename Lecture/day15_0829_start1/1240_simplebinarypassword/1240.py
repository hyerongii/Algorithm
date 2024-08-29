import sys
sys.stdin = open("input.txt", "r")

dict = {
        "0001101": "0",
        "0011001": "1",
        "0010011": "2",
        "0111101": "3",
        "0100011": "4",
        "0110001": "5",
        "0101111": "6",
        "0111011": "7",
        "0110111": "8",
        "0001011": "9"
        }

def find_startpoint():
    # 딕셔너리에 맞는 숫자 찾을때까지 돌리기
    for i in range(M - 56 + 1):
        password = ""
        for j in range(9):
            if len(password) == 8:
                return password
            # 시작할 때 맞는 키가 있으면 8숫자 다 key에 있는지 확인 없으면 다시 i 이동
            if password_bin[i + 7*j:i + 7*j + 7] in dict.keys():
                password += dict[password_bin[i + 7*j:i + 7*j + 7]]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    # 1. 주어진 비밀번호 찾을 수 있는 정보 행만 빼내기
    # 2. 7비트 -> 10진수 딕셔너리 만들기
    # 3. 행 자르면서 10진수로 바꾸기

    # 정보행만 빼냄 -> password
    zero_str = "0"*M
    for i in range(N):
        if arr[i] != zero_str:
            password_bin = arr[i]
            break

    password = find_startpoint()
    total_v = 0
    sum_v = 0
    for i in range(8): # 0 ~ 7
        # 실질적으로 짝수자리 일때 다 더해서 *3
        if not i % 2:
            sum_v += int(password[i])
        else:
            total_v += int(password[i])
    total_v += sum_v*3

    if total_v % 10:
        result = 0
    else:
        result = sum(list(map(int, list(password))))

    print(f'#{tc} {result}')




