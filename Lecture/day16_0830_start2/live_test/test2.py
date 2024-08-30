'''
16진수 문자로 이루어진 1차 배열이 주어질 때 앞에서부터 7bit씩 묶어 십진수로 변환하여 출력해 보자

입력
0F97A3


2진수: 000011111001011110100011
answer: 7, 101, 116, 3
'''

hex_to_bin = {f'{i:X}': f'{i:04b}' for i in range(16)}
hex_num = input()
bin_num = ""
for num in hex_num:
    bin_num += hex_to_bin[num]

for i in range(len(bin_num)//7+1):
    num = bin_num[7*i:7*i+7]
    print(int(num, base=2))