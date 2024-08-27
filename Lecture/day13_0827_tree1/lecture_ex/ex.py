'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

# 전위 순회 구현 (나 -> 좌 -> 우)
def pre_order(T):
    if T:
        print(T, end= " ")
        pre_order(left[T])
        pre_order(right[T])

N = int(input()) # 1번부터 N번까지인 정점
E = N-1 # 간선
arr = list(map(int, input().split()))
left = [0]*(N+1) # 1번부터 인덱스로 생각할라고
right = [0]*(N+1)
par = [0]*(N+1) # 부모, root 찾을라고

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]  # 입력 규칙이 처음이 부모 - 자식 순이어서
    if left[p] == 0: # 왼쪽 비었으면 왼쪽에 우선순위 먼저
        left[p] = c
    else:
        right[p] = c # 그다음 오른쪽 넣어줌
    par[c] = p # 자녀 인덱스에 부모 인덱스 값으로 넣어줌

c = N  # 마지막 노드
while par[c] != 0:      # 부모가 있으면
    c = par[c]          # 부모를 새로운 자식으로 두고
root = c                # 더이상 부모가 없으면 root
print(root)             # 루트 출력
pre_order(root)


#### 울반 강사님이 풀어준 방법

def search(node):
    if node != 0: # 그 node 값이 0이 아니라면
        print(node) # 전위순회면...
        search(tree[node][0]) # 왼쪽을 조사
        search(tree[node][1]) # 오른쪽을 조사


N = int(input())        # 1번부터 N번까지인 정점
E = N-1
arr = list(map(int, input().split()))

# tree 정보를 입력 할 수 있도록 하겠다.
# tree 리스트의 index 번호 -> 부모 노드의 번호
# tree[parent] 위치의 리스트의 0번째 - 왼쪽자식
# tree[parent] 위치의 리스트의 1번째 - 오른쪽 자식

tree = [[0, 0] for _ in range(N)] # 0번 노드 안쓸거임

for i in range(len(arr)): # 간선 정보 주어짐
    # 부모 자식 관계를 한번에 나타내고 싶음
    if not tree[arr[2*i]][0]:
        tree[arr[2*i]][0] = arr[2*i+1]
    else:
        tree[arr[2*i]][1] = arr[2*i+1]
