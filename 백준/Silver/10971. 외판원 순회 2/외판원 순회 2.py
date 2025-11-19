import sys
input = sys.stdin.readline

n=int(input())
arr=[]

for _ in range(n):
    arr.append(list(map(int,input().split())))

min_cnt=1e9
visited=[False]*n
seq=[]

def dfs():
    global min_cnt
    if len(seq)==n:
        cnt=0
        safe=True
        for i in range(n-1):
            if arr[seq[i]][seq[i+1]]==0:
                safe=False

                break
            cnt+=arr[seq[i]][seq[i+1]]

        if safe:
            if arr[seq[-1]][seq[0]]!=0:
                cnt+=arr[seq[-1]][seq[0]]
        
                min_cnt=min(min_cnt,cnt)
            #print(*seq,cnt)
        return
    

    for i in range(n):
        if not visited[i]:
            seq.append(i)
            visited[i]=True
            dfs()
            seq.pop()
            visited[i]=False

dfs()
print(min_cnt)