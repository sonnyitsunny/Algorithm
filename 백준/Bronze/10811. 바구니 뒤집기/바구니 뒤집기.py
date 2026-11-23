N,M=map(int,input().split())



b=[]
for i in range(1,N+1):
    b.append(i)

for _ in range(M):
    s,e=map(int,input().split())
    
    front=b[:s-1]
    mid=b[s-1:e]
    back=b[e:]
    mid.reverse()
    b=front+mid+back
print(*b)