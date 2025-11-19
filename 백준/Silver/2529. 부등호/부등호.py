import sys
input = sys.stdin.readline



k=int(input())
arr=list(input().split())

visited=[False]*10

max_res=0
min_res=1e12
max_str=""
min_str=""



def dfs(nums,depth):
    global max_res
    global min_res
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
            int_nums=int(str_nums)
            #최대
            if int_nums>max_res:
                max_res=int_nums
                max_str=str_nums
            if int_nums<min_res:
                min_res=int_nums
                min_str=str_nums

        return

    for i in range(10):
        if not visited[i]:
            visited[i]=True
            dfs(nums+[i],depth+1)
            visited[i]=False







dfs([],0)
print(max_str)
print(min_str)