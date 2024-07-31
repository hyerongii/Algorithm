

arr1 = [0] * 3

# 행 2 열 3인 0을 값으로 가지는 2차원 배열 만드는 법
arr2 = [[0] * 3 for _ in range(2)]
print(arr1)
print(arr2)

# 행 우선 순회 : 한줄로 원소 나열
for i in range(2):
    for j in range(3):
        print(arr2[i][j], end = '')


arr = [[1,2,3], [4,5,6]]
print(len(arr))      # 2 , 행의 수
print(len(arr[0]))   # 3 , 열의 수


# 주의!! 이렇게 만들면 안됨
arr = [[0]*3]*2
print(arr)  # [[0,0,0],[0,0,0]]
arr[0][0] = 1
print(arr)  # [[1,0,0],[1,0,0]]

arr = [[2,1,1],[1,2,2]]
max_v = 0
for i in range(len(arr)):
    sum_v = 0
    for j in arr[i]:
        sum_v += j
    if max_v < sum_v:
        max_v = sum_v
print(max_v)