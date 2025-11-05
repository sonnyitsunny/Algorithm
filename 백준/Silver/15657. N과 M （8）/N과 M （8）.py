import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N,M=map(int,input().split())
nums=list(map(int,input().split()))


nums.sort()

def dfs(arr,start):
    if len(arr)==M:
        print(*arr)
        return
    
    for i in range(start,N):
        
        dfs(arr+[nums[i]],i)
        



dfs([],0)