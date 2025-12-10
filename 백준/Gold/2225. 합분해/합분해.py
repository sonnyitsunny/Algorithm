import sys
input = sys.stdin.readline

N,K=map(int,input().split())

dp=[[0]*(K+1) for _ in range(N+1)]

for k in range(1,K+1):
    dp[0][k]=1

for n in range(0,N+1):
    dp[n][1]=1
for n in range(1,N+1):
    for k in range(2,K+1):
        dp[n][k]=(dp[n-1][k]+dp[n][k-1])%1000000000
print(dp[N][K])