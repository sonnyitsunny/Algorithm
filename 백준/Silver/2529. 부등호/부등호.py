import sys
input = sys.stdin.readline



k=int(input())
arr=list(input().split())
visited=[False]*10

max_str=None
min_str=None
res=[]


def dfs(nums,depth):

    if depth==k+1:
        res.append(''.join(map(str,nums)))
        return

    for i in range(10):
        if not visited[i]:
            
            if depth>0:
                op=arr[depth-1]
                if op=='<':
                    if int(nums[depth-1]) > i:
                        continue


                elif op=='>':
                    if int(nums[depth-1]) < i:
                        continue

            visited[i]=True
            dfs(nums+[i],depth+1)
            visited[i]=False



dfs([],0)

res.sort()
print(res[-1])
print(res[0])