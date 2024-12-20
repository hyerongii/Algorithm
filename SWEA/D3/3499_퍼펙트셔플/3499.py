import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(input().split())
    mid = N//2  # 3
    shuffle = []
    if N % 2 == 0:
        for i in range(mid): # 0 1 2
            shuffle.append(card[i]) # 0
            shuffle.append(card[i+mid]) # 3
        print(f'#{tc} {" ".join(shuffle)}')
    else:
        for j in range(mid):
            shuffle.append(card[j]) # 0 1 2
            shuffle.append(card[j+mid+1]) # 4 5 6
        shuffle.append(card[mid]) # 3
        print(f'#{tc} {" ".join(shuffle)}')

# 프린트 함수 써서 에러인가;;
#     # 카드가 짝수개일때, 돌아가면서 출력
#     if N % 2 == 0:
#         print("#"+str(tc), end=" ")
#         for i in range(mid):
#             print(card[i], end=" ")
#             print(card[i+mid], end=" ")
#     # 카드가 홀수개일때, 먼저 놓는 쪽(왼쪽리스트)에 카드 하나 더 넣어주기
#     else:
#         print("#"+str(tc), end=" ")
#         for i in range(mid):
#             print(card[i], end=" ")
#             print(card[i+1+mid], end=" ")
#         print(card[mid])
#     print()
