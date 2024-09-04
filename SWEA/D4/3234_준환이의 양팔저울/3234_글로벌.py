import sys
sys.stdin = open('input.txt')

# 완전 탐색하는 연습 충분히 하기
# 가능한 모든 경우
def f(i, N, lw, rw):    # i: 저울에 올린 추 개수, N: 추 개수, lw: 왼쪽 무게, rw: 오른쪽 무게
    global cnt
    if lw < rw:         # 오른쪽 무게가 더 큰 조건이라면
        return          # 조건에 위배되는 경우
    elif i == N:        # 모든 추를 올린 경우
        cnt += 1
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]    # i 순서에 올린 추 번호 p[i]정하기
            f(i+1, N, lw + arr[p[i]], rw)   # p[i] 추를 왼쪽에 올린 경우
            f(i+1, N, lw, rw + arr[p[i]])   # p[i] 추를 오른쪽에 올린 경우
            p[i], p[j] = p[j], p[i]    # p[i] 추를 다른 순서에 사용할 수 있도록 함

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    p = [i for i in range(N)]        # 추를 올리는 순서를 저장한 순열로 만들기

    cnt = 0  # 조건에 맞게 추를 올리는 경우의 수
    f(0, N, 0, 0)
    print(f'{tc} {cnt}')