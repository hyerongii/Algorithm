def snail(n):
    if n == 1:
        return [[1]]
    else:
        snail_array = [[0 for i in range(n)] for j in range(n)]
        snail_array[0][0] = 1
        i = 0
        j = 0
        direction = "right"
        for k in range(2, n**2 + 1):   # 2, 3, 4, 5, 6 ,,, 차례로 넣는 숫자
            if direction == "right":
                if j + 1 < n and snail_array[i][j + 1] == 0:
                    j += 1
                    snail_array[i][j] = k
                else:
                    direction = "down"
                    i += 1
                    snail_array[i][j] = k
            elif direction == "down":
                if i + 1 < n and snail_array[i + 1][j] == 0:
                    i += 1
                    snail_array[i][j] = k
                else:
                    direction = "left"
                    j -= 1
                    snail_array[i][j] = k
            elif direction == "left":
                if j - 1 >= 0 and snail_array[i][j - 1] == 0:
                    j -= 1
                    snail_array[i][j] = k
                else:
                    direction = "up"
                    i -= 1
                    snail_array[i][j] = k
            elif direction == "up":
                if i - 1 >= 0 and snail_array[i - 1][j] == 0:
                    i -= 1
                    snail_array[i][j] = k
                else:
                    direction = "right"
                    j += 1
                    snail_array[i][j] = k
        return snail_array

for t in range(1, int(input())+1):
    n=int(input())
    print(f'#{t}')
    arr=snail(n)
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()