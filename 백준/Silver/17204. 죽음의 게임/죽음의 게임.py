

N,K=map(int,input().split())

M=0
visited=[False]*N
cur=0
visited[cur]=True

nxt=[]
for _ in range(N):
    nxt.append(int(input()))

while True:
    cur=nxt[cur]
    M+=1

    if cur == K:
        print(M)
        break
    if visited[cur]:
        print(-1)
        break
    visited[cur]=True
