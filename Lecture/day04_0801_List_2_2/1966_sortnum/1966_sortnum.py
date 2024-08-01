import sys
sys.stdin = open("input.txt", "r")

def selection_sort(a, n):
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if a[min_idx] >= a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{test_case} {" ".join(list(map(str, selection_sort(arr, N))))}')
