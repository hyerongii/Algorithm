import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    N = arr[0]
    info_lst = arr[1:]

    orange = []
    blue = []

    # B 2 O 1 O 2 B 4 -> 짝수번:로봇이름, 홀수번:버튼위치
    # B 는 B 끼리 O 는 O 끼리 묶기
    for i in range(0,len(info_lst),2):

        robot = info_lst[i]
        move = int(info_lst[i+1])

        B_count = []

        # 오렌지랑 블루를 버튼 장소로 이동시킨 후 버튼 누를 때 "*" 표시
        if robot == "O":
            O_count = 0
            for _ in range(move):
                orange.append(1)
                O_count += 1
            orange.append("*")

        elif robot == "B":
            B_count = move

            for _ in range(move):
                blue.append(1)
            blue.append("*")

    result = 0
    if len(orange)

    print(f'o:{orange}, b:{blue}')






