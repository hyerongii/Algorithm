import sys
sys.stdin = open("input.txt", "r")

# 델타 탐색을 할 때는 무조건 dxy를 만들고 시작하자.
dxy = [[1,0],[0,-1],[0,1]]

def search_ladder(x,y):

    # 지나왔다는 것을 표시하기 위한 변수, 원본을 훼손하지 않고, 방문 체크
    # 지나 갈 때 마다 그 index를 1로 바꿔주기
    visited = [[0] * BLOCK_SIZE for _ in range(BLOCK_SIZE)]
    
    visited[x][y] = 1 # 시작 지점을 방문체크함

    # x 좌표는 행, y 좌표는 열
    # 마지막 행(99)에 도착할 때 까지 델타 검색을 진행한다.
    while x != BLOCK_SIZE-1:
        # 3방향으로 탐색해야한다.
        # x는 현재 좌표, nx 는 현재 델타만큼 이동한 후의 좌표

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            # 이동하려는 좌표가 범위를 벗어난 경우
            if nx < 0 or nx >= BLOCK_SIZE or ny <0 or ny >= BLOCK_SIZE: continue
            
            # 사다리가 아닌 경우 data[nx][ny] 값이 1이면 True / 0이면 False
            if not data[nx][ny]: continue

            # 이미 방문한 경우 값이 1이면 True / 0이면 False
            if visited[nx][ny]: continue

            # 이 지점에 도착한 경우는 범위를 만족하고, 사다리고, 방문하지 않았다
            # 현재 좌표를 방문한 것으로 생각한다
            visited[x][y] = 1

            # 그 다음 좌표로 진행
            x, y = nx, ny
    
    if data[x][y] == 2:
        return True
    
    return False

for _ in range(1,11):
    tc = int(input())
    BLOCK_SIZE = 100
    data = [list(map(int, input().split())) for _ in range(BLOCK_SIZE = 100)]

    result = -1
    for j in range(BLOCK_SIZE):

        '''
        early returen
        조건을 걸고 바로 리턴 시키는 것

        [0,1,2,3,4]
        # 1번 코드 (깊이가 깊어짐)
        if data[0][j] == 1 or data[0][j] == 2 or data[0][j] == 3:
            print("hello")
        
        # 2번 코드 (얼리리턴)
        if data[0][j] == 0:
            continue
        if data[0][j] == 4:
            continue
        print("hello")

        -> 이렇게 하면 코드가 길어지는 단점있지만 디버깅이 쉬워짐
        '''

        if data[0][j] == 0 : 
            continue
        # 여기에 도달한 친구들은 첫 번째 줄에서의 사다리
        # 0, j에서 시작했을 때, 목적지에 도달하는지 확인하는 함수
        # 이 함수는 True, False 반환
        if search_ladder(0,j):
            # 제대로 도달한 친구는 아래 if문 코드를 돌린다
            # 제대로 도달했을 때의 시작점은 j이기 때문에, 최종 결과에 저장한다.
            result = j
            break # if 문을 탈출하는게 아니고, 제일 가깝게 있는 for/while문 탈출

    print(f'{tc} {result}')