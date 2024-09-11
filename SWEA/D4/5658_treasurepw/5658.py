import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # N: 숫자 개수 K: 크기 순서
    N, K = map(int, input().split())
    string = input()

    password = set()
    # 돌리면서 set에 넣기
    for i in range(N/4): # 0 1 2
        for j in range(4):
            password.add(string[i:i+3])
