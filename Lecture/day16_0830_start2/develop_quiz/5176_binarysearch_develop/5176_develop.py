import sys
sys.stdin = open("input.txt", "r")

def search(node):
    global count
    # 노드개수 채울때까지
    if node < 9:
        # 중위 순회 start
        search(node*2)
        # 현재 노드 번호에 값 삽입 (중위 순회 순서 값이 들어가게됨)
        count += 1
        tree[node] = count
        search(node*2+1)

T = int(input())
for tc in range(1, T+1):
    password = input()
    # 처음 숫자
    N = int(password[0])
    # 뒷 16자리 문자열
    hex_num = password[1:]

    num_lst = []
    # 16자리 암호 문자열 -> 2자리씩 10진수로 변환
    for i in range(8):
        dec_num = int(hex_num[2*i:2*i+2], base=16)
        num_lst.append(dec_num)

    # 비밀번호 10진수로 변환한 후 salt 값 각각 빼주기
    for num in range(1, 9):
        num_lst[num-1] -= num * N

    # 노드 번호는 순서대로 부여
    # 이진 탐색 트리는 중위순회 순으로 값 저장됨

    # tree 0 배열로 생성
    tree = [0] * 9
    # 순서대로 부여된 노드 번호 카운트
    count = 0
    # 트리 탐색
    search(1)

    print(f'#{tc}', end=" ")
    for i in range(1, 9):
        print(num_lst[tree[i]-1]%10, end="")
    print()

