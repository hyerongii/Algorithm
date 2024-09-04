from collections import deque
def finding_parent(kid, parent_lst):
    q = deque()
    q.append(kid)
    while q:
        n = q.popleft()
        parent_lst.append(n)
        if tree[n] == 0:
            return parent_lst
        q.append(tree[n])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    V = N-1

    # 간선 정보 받으면서 tree에 넣어주기 - 리스트 사용
    # 부모 자식 순서로 들어옴,,,, 근데 N 만번인데 괜찮을지,,,
    tree = [0]*(N+1)

    for _ in range(V):
        A, B = map(int, input().split())
        # 자식을 인덱스로 생각하고 부모를 자식 인덱스에 값으로 표시하기
        tree[B] = A

    # 공통 조상을 구할 두 노드
    node1, node2 = map(int, input().split())
    first_lst = []
    finding_parent(node1, first_lst)
    second_lst = []
    finding_parent(node2, second_lst)

    answer = 0
    for node in first_lst:
        if node in second_lst:
            answer = node
            break

    print(node)


