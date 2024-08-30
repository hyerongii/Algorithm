'''
16진수 문자로 이루어진 1차 배열이 주어질 때, 왼쪽부터 순차적으로 암호비트패턴을 찾아 차례대로 출력하시오. 암호는 연속되어있다.

입력
0DEC
0269FAC9A0


2진수: 0000110111101100
answer: 7, 101, 116, 3
'''

bin_to_dec = {
        "001101": 0,
        "010011": 1,
        "111011": 2,
        "110001": 3,
        "100011": 4,
        "110111": 5,
        "001011": 6,
        "111101": 7,
        "011001": 8,
        "101111": 9
        }

hex_to_bin = {f'{i:X}': f'{i:04b}' for i in range(16)}

hex_num = input()
bin_num = ""
for num in hex_num:
    bin_num += hex_to_bin[num]

idx = 0
while idx <= len(bin_num) - 6:
    target = bin_num[idx:idx+6]
    if bin_to_dec.get(target) != None: # True , False 아닐때 값이 0포함일 때,,
        print(bin_to_dec[target], end=" ")
        idx += 6
    else:
        idx += 1
