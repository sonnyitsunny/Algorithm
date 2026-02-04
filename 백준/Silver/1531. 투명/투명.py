
N,M=map(int,input().split())

board=[[0]*(100) for _ in range(100)]
ans=0

for _ in range(N):
    sr,sc,er,ec = map(int,input().split())
    for i in range(sr-1,er):
        
        for j in range(sc-1,ec):
            #print(0)
            board[i][j]+=1

for i in range(100):
    for j in range(100):
        if board[i][j]>M:
            ans+=1

# for r in board:
#     print(r)
print(ans)