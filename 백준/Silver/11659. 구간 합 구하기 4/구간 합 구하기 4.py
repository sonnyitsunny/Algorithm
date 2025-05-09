import sys

input=sys.stdin.readline

n,m=map(int,input().split())
d=[0]*(n+1)
arr=list(map(int,input().split()))
for i in range(0,n):
    d[i+1]=d[i]+arr[i]

for _ in range(m):
    i,j=map(int,input().split())
    print(d[j]-d[i-1])
    