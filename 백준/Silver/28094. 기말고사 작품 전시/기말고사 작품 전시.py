T=int(input())
for _ in range(T):
    N,M=map(int,input().split())

    w=[[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        V,A,B=map(int,input().split())
        w[A][B]+=V

    used = [False] * (N+1)
    order=[]

    best=-10**30
    cnt=0

    def dfs(score):
        global best,cnt
        if len(order)==N:
            if score>best:
                best=score
                cnt=1
            elif score==best:
                cnt+=1
            return 

        for x in range(1,N+1):
            if used[x]:
                continue

            

            add=0
            for y in order:
                add+=w[y][x]
            used[x]=True
            order.append(x)
            dfs(score+add)
            order.pop()
            used[x]=False
    dfs(0)
    print(best,cnt)