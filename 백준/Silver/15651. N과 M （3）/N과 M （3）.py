import sys

input = sys.stdin.readline


N,M=map(int,input().split())
path=[]

def dfs(depth):
    if depth==M:
        print(' '.join(map(str,path)))
        return
    
    for num in range(1,N+1):
        path.append(num)
        dfs(depth+1)
        path.pop()
dfs(0)