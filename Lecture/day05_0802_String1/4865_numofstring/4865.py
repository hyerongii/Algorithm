import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1 = set(input())
    str2 = list(input())

    # str2에 글자 있는지 카운트
    count = {}
    for x in str1:
        count[x] = 0

    for x in str1:
        for i in range(len(str2)):
            if x == str2[i]:
                count[x] += 1
                
    max_count = 0
    # value 중에 가장 큰 값 출력
    for v in count.values():
        if v >= max_count:
            max_count = v
    
    print(f'#{test_case} {max_count}')