import sys
sys.stdin = open("input.txt", "r")

def search(node):
    global result
    if node != 0:
        search(tree[node][0])
        result.append(node)
        search(tree[node][1])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [[0, 0] for _ in range(N+1)]

    # 트리 만들어주기
    for i in range(1, N//2+1):
        tree[i][0] = 2*i
        tree[i][1] = 2*i+1
    if N % 2 == 0:
        tree[N//2][1] = 0

    result = []
    search(1)

    print(f'#{tc} {result.index(1)+1} {result.index(N//2)+1}')

    # 왼쪽 서브트리의 루트 <현재 노드 <오른쪽 서브 트리의 루트
    # 완전이진트리이기 때문에 가능
    # 1. 중위 순회로 tree 만들어주기 (일단 값을 저장)
    # 2. 루트값 뽑아내기, bfs로 돌아가면서 N//2 노드에 저장된 값 출력하기





