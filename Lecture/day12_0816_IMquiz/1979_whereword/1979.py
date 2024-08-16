import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    # N: 퍼즐크기 K: 단어길이
    N, K = map(int, input().split())

    # arr: 입력받은 퍼즐 제로패딩하고 시작하기
    arr = [list(map(int, input().split())) for _ in range(N)]
    new_arr = [[0]*(N+2) for _ in range(N+2)]
    for i in range(N):
        for j in range(N):
            new_arr[i+1][j+1] = arr[i][j]

    # 흰색: 1, 검은색: 0
    # 가로 또는 세로의 연속된 흰색길이가 단어길이와 같아야 정답 카운트
    # 가로k or 세로k 윈도우 돌려서 찾기
    # 찾는 값 형태
    answer = [0] + [1]*K + [0]
    result = 0
    for k in range(N+1):
        for l in range(N+2-len(answer)+1):
            if new_arr[k+1][l:l+len(answer)] == answer:
                result += 1

    newnew_arr = [[0]*(N+2) for _ in range(N+2)]

    for i in range(N+2):
        for j in range(N+2):
            newnew_arr[i][j] = new_arr[j][i]

    for i in range(N+1):
        for j in range(N+2-len(answer)+1):
            if newnew_arr[i+1][j:j+len(answer)] == answer:
                result += 1

    print(f'#{tc} {result}')