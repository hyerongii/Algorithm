import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    num = float(input())
    result = ""
    # 받아서 -1 ~ -13 까지..
    for i in range(-1, -14, -1):
        if num != 0:
            if num >= (2**i):
                num -= 2**i
                result += "1"
            else:
                result += "0"
        else:
            break
    if len(result) >= 13:
        result = "overflow"
    print(f'#{tc} {"".join(result)}')