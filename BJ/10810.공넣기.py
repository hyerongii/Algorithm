N, M = map(int, input().split())
basket_lst = [0]*(N+1)

# M줄 동안 반복
for x in range(M):
    i, j, k = map(int, input().split())
    for y in range(i, j+1):
        basket_lst[y] = k

print(*basket_lst[1:])