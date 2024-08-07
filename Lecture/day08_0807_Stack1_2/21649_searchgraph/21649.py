import sys
sys.stdin = open("input.txt", "r")

def dfs(current, adjM, visited):
    visited[current] = True # 현재 정점 방문했다고 표시
    current_lst.append(current+1)
    
    for i in range(len(adjM)): # 모든 정점에 대해
        if adjM[current][i] and not visited[i]: # 정점과연결&방문안했으면
            dfs(i, adjM, visited)

V, E = map(int, input().split())
arr = list(map(int, input().split()))

# 인접행렬 생성하는 과정
adjM = [[0] * (V+1) for _ in range(V+1)]

# 점과 점이 연결되어 있는 개수, 간선, E
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adjM[v1][v2] = 1 # 그래프 방향 있으면 이것만 추가
    adjM[v2][v1] = 1 # 그래프에 방향이 없어서 추가

# 방문 체크 배열 초기화
visited = [False] * V  # 모든 정점 아직 방문하지 않음
current_lst = []

# 시작 정점 : 0
dfs(0, adjM, visited)

print(f'#1 {"-".join(list(map(str, current_lst)))}')