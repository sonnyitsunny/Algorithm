import sys
input = sys.stdin.readline

N,M=map(int,input().split())
A=[]
for _ in range(N):
    A.append(list(map(int,input().strip())))
B=[]
for _ in range(N):
    B.append(list(map(int,input().strip())))


def op(x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            A[i][j]=1-A[i][j]

cnt=0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j]!=B[i][j]:
            op(i,j)
            cnt+=1
if A==B:
    print(cnt)
else:
    print(-1)