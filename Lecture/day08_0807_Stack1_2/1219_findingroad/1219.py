import sys
sys.stdin = open("input.txt", "r")

def dfs(current, adjL, visited):
    visited[current] = True
    current_lst.append(current)

    for i in range(len(adjL)):
        if adjL[current][i] and not visited[i]:
            dfs(i, adjL, visited)

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc, E = map(int, input().split())
    # 최대 정점의 개수
    V = 100
    arr = list(map(int, input().split()))

    adjL = [[0]*V for _ in range(V)]

    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        adjL[v1][v2] = 1

    visited = [False] * V
    current_lst = []

    dfs(0, adjL, visited)
    
    if 99 in current_lst:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
    

    