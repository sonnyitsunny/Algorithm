import sys
input = sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))

max_cnt=0

visited=[False]*n
temp=[]

def dfs():

    global max_cnt
    if len(temp)==n:
        cnt=0
        for i in range(n-1):
            cnt+=abs(temp[i]-temp[i-1])

        max_cnt=max(cnt,max_cnt)
        return
    

    for i in range(n):
        if not visited[i]:
            temp.append(arr[i])
            visited[i]=True
            dfs()

            temp.pop()
            visited[i]=False








dfs()
print(max_cnt)