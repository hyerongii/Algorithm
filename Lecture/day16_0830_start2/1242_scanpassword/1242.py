import sys
sys.stdin = open('input.txt')

bin_dict = {}
dec_dict = {}


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    '''
    1. 암호있는 줄 분리
    2. 암호 따로따로 분리
    3. 암호 처리하는 함수 호출 -> 16진수-2진수 2진수-10진수 딕셔너리 필요
    4. 변환된 암호 검증코드 인지 확인 
    '''

