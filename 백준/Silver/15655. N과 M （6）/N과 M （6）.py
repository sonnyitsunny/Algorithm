import sys

input = sys.stdin.readline


N,M=map(int,input().split())
arr=list(map(int,input().split()))
path=[]
arr.sort()


def dfs(depth,arr):
    if depth==M:
        print(' '.join(map(str,path)))
        return
    
    for i in range(len(arr)):
        path.append(arr[i])
        dfs(depth+1,arr[i+1:])
        path.pop()
dfs(0,arr)