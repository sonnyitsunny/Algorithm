import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N,M=map(int,input().split())
nums=list(map(int,input().split()))


nums.sort()

def dfs(idx,arr):
    if len(arr)==M:
       

        print(*arr)
            
        return
       
    prev=0
    for i in range(idx,N):
        if nums[i]!=prev:
            dfs(i+1,arr+[nums[i]])
            prev=nums[i]
        else:
            continue
        



dfs(0,[])