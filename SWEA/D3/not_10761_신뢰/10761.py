import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    N = arr[0]
    info_lst = arr[1:]

    # 오렌지랑 블루 스택만들기 current 번호, 버튼 누르기 전 움직인 거리
    orange = [1,0]
    blue = [1,0]

    # 누르는거 1초 걸림
    push = 1
    cnt = 0

    # B 2 O 1 O 2 B 4 -> 짝수번:로봇이름, 홀수번:버튼위치
    for i in range(0,len(info_lst),2):
        robot = info_lst[i]
        move = int(info_lst[i+1])

        # 오렌지면,
        if robot == "O":
            # 현재위치에서 이동해야할 곳 까지 이동
            orange[1] = move - orange[0]
            # 푸쉬 누르기 전에 누를 타이밍이면 1초 기다리기
            if blue[1] != 0 and blue[1] == orange[1]:
                orange[1] += 1
            else:
                orange[1] += push
            # 그리고 현재위치 변경
            orange[0] = move

        # 블루면,
        elif robot == "B":
            # 현재위치에서 이동해야할 곳 까지 이동
            blue[1] = move - blue[0]
            # 푸쉬 누르기 전에 누를 타이밍이면 1초 기다리기
            if orange[1] != 0 and blue[1] == orange[1]:
                blue[1] += 1
            else:
                blue[1] += push
            # 그리고 현재위치 변경
            blue[0] = move

    print(f'o:{orange}, b:{blue}')






