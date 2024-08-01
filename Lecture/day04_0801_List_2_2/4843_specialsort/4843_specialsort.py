import sys
sys.stdin = open("input.txt", "r")

# 내장함수사용금지

def find_max_min(arr):
    
    arr_max = arr[0]
    arr_min = arr[0]

    for i in range(len(arr)):
        if arr_min >= arr[i]:
            arr_min = arr[i]
        if arr_max <= arr[i]:
            arr_max = arr[i]
    
    return [arr_max, arr_min]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    array = list(map(int, input().split()))

    new_list = []

    while len(array) != 0:  
        new_list += find_max_min(array)
        array.remove(find_max_min(array)[0])
        array.remove(find_max_min(array)[1])
    
    print(f'#{test_case} {" ".join(list(map(str, new_list[:10])))}')

