def selection_sort(arr, N):
    for i in range(N-2):
        min_idx = i
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

A = [2, 7, 5, 3, 4, 0]
B = [4, 3, 2, 1, 0]
print(selection_sort(A, len(A)))
print(selection_sort(B, len(B)))
