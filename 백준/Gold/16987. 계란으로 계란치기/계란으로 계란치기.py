import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N=int(input())
eggs=[list(map(int,input().split())) for _ in range(N)]
res=0

def dfs(idx):
    global res

    if idx==N:
        broken=0
        for d,w in eggs:
            if d<=0:
                broken+=1
        res=max(res,broken)
        return
    
    if eggs[idx][0]<=0:
        dfs(idx+1)
        return
    
    hit=False

    for j in range(N):
        if j==idx or eggs[j][0]<=0:
            continue
        hit=True

        eggs[idx][0]-=eggs[j][1]
        eggs[j][0]-=eggs[idx][1]

        dfs(idx+1)

        eggs[idx][0]+=eggs[j][1]
        eggs[j][0]+=eggs[idx][1]

    if not hit:
        dfs(idx+1)

dfs(0)
print(res)