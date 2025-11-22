import sys
input = sys.stdin.readline

N=int(input())

lines=[]
for _ in range(N):
    a,b=map(int,input().split())
    lines.append((a,b))

lines.sort()
arr=[b for _,b in lines]

dp=[1]*N

for i in range(N):
    for j in range(i):
        if arr[j]<arr[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(N-max(dp))