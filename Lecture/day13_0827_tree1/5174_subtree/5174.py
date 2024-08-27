import sys
sys.stdin = open("input.txt", "r")

def search(node):
    global count
    if node != 0: # 그 node 값이 0이 아니라면
        count += 1 # 카운트 세주기
        search(tree[node][0])
        search(tree[node][1])

T = int(input())
for tc in range(1, T+1):
    E, root = map(int, input().split())  # 간선 수, 찾는 루트
    arr = list(map(int, input().split()))
    N = E+1  # 노드 수

    tree = [[0, 0] for _ in range(N+1)] # 0,0 안쓸거니까 노드수 +1

    # tree 리스트에 부모,자식 다 넣기
    for i in range(len(arr)//2):
        if not tree[arr[2*i]][0]:
            tree[arr[2*i]][0] = arr[2*i+1]
        else:
            tree[arr[2*i]][1] = arr[2*i+1]

    count = 0
    search(root)
    print(f'#{tc} {count}')
