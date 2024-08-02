import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1 = input()
    N1 = len(str1)
    str2 = list(input())
    N2 = len(str2)
    result = 0

    for i in range(0, N2-N1+1):
        if str1 == "".join(str2[i:i+N1]):
            result = 1
    
    print(f'#{test_case} {result}')
