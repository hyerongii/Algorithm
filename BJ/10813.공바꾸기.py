N,M = map(int, input().split())
basket = [0]*(N+1)

for idx in range(1, N+1):
    basket[idx] = idx

for x in range(M):
    i,j = map(int, input().split())
    ball_i, ball_j = basket[i], basket[j]
    basket[i] = ball_j
    basket[j] = ball_i

print(*basket[1:])