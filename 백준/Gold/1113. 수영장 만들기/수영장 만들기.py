import heapq
N,M=map(int,input().split())
pool=[]
for _ in range(N):
    pool.append(list(map(int,input())))

visited=[[False]*M for _ in range(N)]
hq=[]
for r in range(N):
    for c in [0,M-1]:
        visited[r][c]=True
        heapq.heappush(hq,(pool[r][c],r,c))

for r in [0,N-1]:
    for c in range(0,M):
        if not visited[r][c]:
            visited[r][c]=True
            heapq.heappush(hq,(pool[r][c],r,c))

water=0

dr=[-1,1,0,0]
dc=[0,0,-1,1]


while hq:
    h,r,c = heapq.heappop(hq)

    for k in range(4):
        nr,nc= r+dr[k],c+dc[k]
        if 0<=nr<N and 0<=nc<M and not visited[nr][nc]:
            visited[nr][nc]=True
            nh=pool[nr][nc]
            if nh<h:
                water+=(h-nh)
            heapq.heappush(hq,(max(h,nh),nr,nc))
print(water)