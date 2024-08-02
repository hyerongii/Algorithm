import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    word = list(input())
    N = len(word)
    result = 1
    
    # 짝수
    for i in range(N//2):
        if word[i] != word[N-1-i]:
            result = 0
            break
    
    print(f'#{test_case} {result}')