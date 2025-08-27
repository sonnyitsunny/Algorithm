import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

result=[]

N = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

def check(a,b):
    if a<0:
        return -((-a)//b)
    return a//b

def dfs(idx,cur,p,m,x,d):
    if idx==N:
        result.append(cur)
        return
    
    nxt=nums[idx]

    if p>0:
        dfs(idx+1,cur+nxt,p-1, m, x, d)

    if m>0:
        dfs(idx+1,cur-nxt,p, m-1, x, d)

    if x>0:
        dfs(idx+1,cur*nxt,p, m, x-1, d)

    if d>0:
        dfs(idx+1,check(cur,nxt),p, m, x, d-1)

dfs(1,nums[0],plus, minus, mul, div)
print(max(result))
print(min(result))