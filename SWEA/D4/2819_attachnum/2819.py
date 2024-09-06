import sys
sys.stdin = open('input.txt')

'''
4x4로 고정
각 칸에 0~9 있음

임의의 위치에서 4방향(델타-상하좌우) 여섯번 이동 -> 저장 -> 7자리의 수
한번 거쳤던거 다시 거쳐도 됨 - visited 사용 x
서로 다른 일곱 자리 수들의 개수..

dfs로 풀자 - 부분집합인데 중복 제거 하는... 
'''
dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def dfs(current, num):
    global num_set

    if len(num) == 7:
        num_set.add(num)
        return

    x, y = current
    for dx, dy in dxy:
        nx = dx + x
        ny = dy + y
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            continue
        current = (nx, ny)
        dfs(current, num+arr[nx][ny])

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(str, input().split())) for _ in range(4)]
    num_set = set()
    # 시작점 0,0으로만 해줘가지고 맨날 에러났던 거였어....ㅠㅜㅠㅜㅠㅜㅠㅜㅠㅜㅠ
    for i in range(4):
        for j in range(4):
            dfs((i, j), arr[i][j])
    print(len(num_set))


