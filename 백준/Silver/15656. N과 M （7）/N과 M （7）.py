import sys
input = sys.stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))

arr.sort()
res=[]

def backtrack(depth):
    if depth==m:
        print(*res)
        return
    
    for i in range(n):
        res.append(arr[i])
        backtrack(depth+1)
        res.pop()
backtrack(0)