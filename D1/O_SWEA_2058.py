# import sys
# sys.stdin = open("input.txt", "r")

'''
하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.

[제약 사항]
자연수 N은 1부터 9999까지의 자연수이다. (1 ≤ N ≤ 9999)

[입력]
입력으로 자연수 N이 주어진다.

[출력]
각 자릿수의 합을 출력한다.
'''

input_data = int(input())

data_sum = 0
while input_data>0:
    b=input_data%10
    input_data//=10
    data_sum+=b

print(data_sum)

# 간단한 방법
# T = map(int,str(input()))
# print(sum(T))

