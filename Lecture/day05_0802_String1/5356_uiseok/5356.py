import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = [list(input()) for _ in range(5)]
    new_arr = ""
    
    try:
        for i in range(5):
            for j in range(len(arr[i])):
                new_arr += arr[j][i]
        
        print(f'#{test_case} {new_arr}')

    except:
        pass