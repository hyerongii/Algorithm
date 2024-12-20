import sys
sys.stdin = open('input.txt')


for _ in range(10):  # 10개의 테스트 케이스
    tc, N = map(int, input().split())
    edges = list(map(int, input().split()))
    SIZE, START, END = 100, 0, 99
    result = 0

    def dfs(vertex, visited):
        global result

        if vertex == END:
            result = 1
            return

        visited[vertex] = True

        for adj_vertex in range(SIZE):
            if graph[vertex][adj_vertex] == 0: continue  # 인접하지 않으면 skip
            if visited[adj_vertex]: continue  # 방문한 적이 있으면 skip

            dfs(adj_vertex, visited)


    # 그래프 초기화
    # 인접행렬로 구현
    # 100개의 정점이 있기 때문에 100 * 100 개의 2차원 배열을 할당함
    graph = [[0] * SIZE for _ in range(SIZE)]

    for i in range(0, len(edges), 2):
        graph[edges[i]][edges[i + 1]] = 1

    # DFS 수행
    visited = [False] * SIZE

    '''
    DFS 파라미터로 뭘 해야하는가? 감이 안오면 위 변수 다 집어 넣기
    1. 재귀 호출을 중단하기 위한 파라미터
    => 시작지점이 목표지점에 도달했을 때
    => 목표지점은 고정되어있고, 
    => 시작지점을 파라미터로 건낸다
    2. 누적, 목표까지 계속 가져가고 싶은 값
    => 방문 여부를 확인하는 변수
    '''
    dfs(START, visited)

    print(f'#{tc} {result}')
