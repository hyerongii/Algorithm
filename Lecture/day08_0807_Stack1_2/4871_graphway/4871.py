import sys
sys.stdin = open("input.txt", "r")

def dfs(current, adjL, visited):
    visited[current] = True
    current_lst.append(current)

    for i in range(len(adjL)):
        if adjL[current][i] and not visited[i]:
            dfs(i, adjL, visited)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    
    adjL = [[0]*(V+1) for _ in range(V+1)]

    for _ in range(E):
        v1, v2 = map(int, input().split())
        adjL[v1][v2] = 1   # 화살표 있음

    S, G = map(int, input().split())

    visited = [False] * (V+1)
    current_lst = []

    dfs(S, adjL, visited) 

    if G in current_lst:
        result = 1
    else:
        result = 0
    
    print(f'#{tc} {result}')


    
    

