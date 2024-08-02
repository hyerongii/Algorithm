import sys
sys.stdin = open("input.txt", "r")

def selection_sort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{test_case} {" ".join(list(map(str, selection_sort(arr, N))))}')
