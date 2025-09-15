import sys
input = sys.stdin.readline


n=int(input())

arr=[[0]*101 for _ in range(101)]

di=[0,-1,0,1]
dj=[1,0,-1,0]

for _ in range(n):
    sj,si,dr,g=map(int,input().split())
    tmp=[(si,sj)]
    tmp.append((si+di[dr],sj+dj[dr]))
    for _ in range(g):
        ei,ej=tmp[-1]

        for i in range(len(tmp)-2,-1,-1):
            ci,cj=tmp[i]
            tmp.append((ei-(ej-cj),ej+(ei-ci)))
    
    for i,j in tmp:
        arr[i][j]=1
res=0
for i in range(100):
    for j in range(100):
        if arr[i][j]==arr[i+1][j]==arr[i][j+1]==arr[i+1][j+1]==1:
            res+=1
print(res)