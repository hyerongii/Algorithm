import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = 0
    lst = []
    for _ in range(N):
        # 입력 잘 받아주기
        A, B = map(int, input().split())
        # A가 증가할 때, B 감소면 +1// B 증가할 때, A 감소면 +1
        if lst:
            for a, b in lst:
                if (a < A and b > B) or (a > A and b < B):
                    result += 1
        lst.append((A, B))
    print(f'#{tc} {result}')

# max_A = 1
# max_B = 1
# if max_A <= A:
#     max_A = A
#     if max_B > B:
#         result += 1
#     else:
#         max_B = B
# else:
#     if max_B <= B:
#         result += 1
#     else:
#         max_B = B