import sys
input = sys.stdin.readline



N,M,K=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]

ops=[]
for _ in range(K):
    r,c,s=map(int,input().split())
    ops.append((r,c,s))

answer=1e9

visited=[False]*K
order = []


def rotate(a, r, c, s):
    r -= 1
    c -= 1

    for layer in range(1, s + 1):
        top = r - layer
        left = c - layer
        bottom = r + layer
        right = c + layer

        prev = a[top][left]
 
        # 왼쪽 → 위
        for i in range(top, bottom):
            a[i][left] = a[i+1][left]

        # 아래 → 왼쪽
        for j in range(left, right):
            a[bottom][j] = a[bottom][j+1]

        # 오른쪽 → 아래
        for i in range(bottom, top, -1):
            a[i][right] = a[i-1][right]

        # 위 → 오른쪽
        for j in range(right, left, -1):
            a[top][j] = a[top][j-1]

        a[top][left+1] = prev


def dfs(depth):
    global answer
    if depth==K:
        arr_copy = [row[:] for row in arr]
        for r,c,s in order:
            rotate(arr_copy,r,c,s)
            
        for row in arr_copy:
            answer=min(answer,sum(row))
        return
    
    for i in range(K):
        if not visited[i]:
            visited[i]=True
            order.append(ops[i])
            dfs(depth+1)
            order.pop()
            visited[i]=False



dfs(0)
print(answer)