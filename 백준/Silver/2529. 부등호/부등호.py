import sys
input = sys.stdin.readline



k=int(input())
arr=list(input().split())
visited=[False]*10

max_str=None
min_str=None
res=[]


def dfs(nums,depth):

    global max_str
    global min_str
    check=True
    if depth==k+1:
        for j in range(k):
            if arr[j]=='>':
                if nums[j]<nums[j+1]:
                    check=False
                    break
            elif arr[j]=='<':
                if nums[j]>nums[j+1]:
                    check=False
                    break
        if check:
            str_nums=''.join(map(str,nums))
            res.append(str_nums)

        return

    for i in range(10):
        if not visited[i]:
            visited[i]=True
            dfs(nums+[i],depth+1)
            visited[i]=False







dfs([],0)

res.sort()
print(res[-1])
print(res[0])