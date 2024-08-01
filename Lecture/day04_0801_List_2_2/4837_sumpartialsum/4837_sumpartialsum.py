import sys
sys.stdin = open("input.txt", "r")

T = int(input())
A = list(range(1, 13))
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    lst = []
    result = 0
    for i in range(1, 1 << 12):
        part_list = []
        for j in range(12):
            if i & (1 << j):
                part_list.append(A[j])
        lst.append(part_list)
    for l in lst:
        if sum(l) == K and len(l) == N:
            result += 1
    print(f'#{test_case} {result}')