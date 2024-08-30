class tree:
    def __init__(self, left=0, right=0):
        self.right=right
        self.left=left
    def data(self, d=0):
        self.d=d

def inorder(N):
    if t[N]:
        global cnt
        if t[N].left:inorder(t[N].left)
        t[N].data(pwd[cnt])
        print(pwd[cnt])
        cnt+=1
        if t[N].right:inorder(t[N].right)

if __name__ == '__main__':
    for tc in range(1, int(input())+1):
        arr=input() # 입력값 salt n 배수, salting되어 있는 암호 받기 (총 17글자)
        pwd=[0]*8
        n, arr=int(arr[0]), arr[1:]
        for i in range(8):
            pwd[i]='0x'+arr[2*i:2*(i+1)]
            pwd[i]=int(pwd[i], 16)
            pwd[i]-=(n*(i+1))
        t=[0]*9
        X=8
        cnt=0
        for i in range(1,9):
            if (i*2+1)<=X:
                t[i]=tree(i*2, i*2+1)
            elif (i*2)==X:
                t[i]=tree(i*2)
            else: t[i]=tree()
        
        inorder(1)
        
        for x in range(X):
            print(t[x+1].left, t[x+1].right)
            pwd[x]=str(t[x+1].d%10)
        
        print(f'#{tc} ', *pwd, sep='')