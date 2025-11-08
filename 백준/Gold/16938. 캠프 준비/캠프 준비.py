import sys
input = sys.stdin.readline

N, L, R, X=map(int,input().split())

arr=list(map(int,input().split()))


res=[]

def dfs(nums,total,id):
    

    if len(nums) >= 2 and L <= total <= R and max(nums)-min(nums) >= X:
        res.append(nums)

    for i in range(id,N):
        
        dfs(nums+[arr[i]],total+arr[i],i+1)





#담은 배열, 난이도 합
dfs([],0,0)
print(len(res))