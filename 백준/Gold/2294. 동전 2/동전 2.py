import sys
input = sys.stdin.readline

N,K=map(int,input().split())
INF=1e9
dp=[INF]*(K+1)

#처음에 배열에 저장 -> 집합 -> 배열

#배열 하나씩 꺼내서 K포함까지dp[x]=1 , dp[2*x]==2 ... dp[i*x]=i이런식으로min을 이용해서 더 작은 값 저장

coins=[]
for _ in range(N):
    coins.append(int(input()))
coins=list(set(coins))

for coin in coins:
    for i in range(1,K+1):
        if coin*i<=K:
            dp[coin*i]=min(dp[coin*i],i)

for i in range(1,K+1):
    for coin in coins:
        if i-coin>=1:
            dp[i]=min(dp[i-coin]+1,dp[i])
if dp[K]!=INF:
    print(dp[K])

else:
    print(-1)