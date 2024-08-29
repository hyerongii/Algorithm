import sys
sys.stdin = open("input.txt", "r")

# 16진수를 2진수로 바꾸는 딕셔너리
hex_to_bin = {f'{i:X}': f'{i:04b}' for i in range(16)}

T = int(input())
for tc in range(1, T+1):
    N, hex_num = input().split()
    N = int(N)
    hex_num = list(hex_num)

    print(f'#{tc}', end= " ")
    for num in hex_num:
        print(f'{hex_to_bin[num]}', end="")
    print()

