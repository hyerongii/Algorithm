import sys
sys.stdin = open("input.txt", "r")

def search(node):
    global inorder_lst
    if node != 0:
        search(tree[node][0])
        inorder_lst.append(node)
        search(tree[node][1])

for tc in range(1, 11):
    N = int(input())
    word = [0]*(N+1)
    tree = [[0, 0] for _ in range(N+1)]

    for _ in range(N):
        input_lst = list(input().split())
        # 순서
        order = int(input_lst[0])
        # 인덱스에 알파벳 넣어줌
        # -> 중회순회하는 순서 리스트에 추가 후 그 순서대로 word print 할거임
        word[order] = input_lst[1]
        # 트리에 좌우 값 넣어주기
        if len(input_lst) > 2:
            tree[order][0] = int(input_lst[2])
        if len(input_lst) > 3:
            tree[order][1] = int(input_lst[3])

    # 트리 중회순회 시키기
    inorder_lst = []
    search(1)

    print(f'#{tc}', end=" ")
    for i in inorder_lst:
        print(word[i], end="")
    print()
