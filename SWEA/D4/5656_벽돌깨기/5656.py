import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    # N: 던질벽돌개수 W: 가로칸 H: 세로칸
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]

    # 1. 최소 벽돌
    # - 몇개 남았을지 계산, 2차원 리스트 순회하면서 계산하면 느림
    # - 남은 벽돌 수를 통해 해결됨
    # 2. 현재 벽돌이 다 깨지면 남은 벽돌 없어서 더이상 진행할 필요 없음
    # - 현재 남은 벽돌 수 같이 저장하기
    # 3. N 번 구슬을 쏘자
    # 시작점 : 0번 / 하나도 안깨진 벽돌 수
    # 끝점 : N번 쏘면 끝 / 벽돌이 다 깨지면 끝

