import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N,M=map(int,input().split())
nums=list(map(int,input().split()))


nums.sort()

def dfs(cnt,arr):
    if len(arr)==M:
        print(*arr)  
        return
       
    prev=0
    for i in range(N):
        if prev!=nums[i]:
            prev=nums[i]
            arr.append(nums[i])
            dfs(cnt+1,arr)
            arr.pop()



dfs(0,[])