import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    string = input()

    str_lst = list(string)
    N = len(str_lst)

    data = ['b','p','q','d']    # 0, 1, 2, 3  반대 index는 더해서 N-1 되도록
    mirror_lst = [0]*N
    
    # bdppq -> pqqbd  

    for i in range(N):
        mirror_lst[N-i-1] = data[3-data.index(str_lst[i])]
    
    print(f'#{test_case} {"".join(mirror_lst)}')
