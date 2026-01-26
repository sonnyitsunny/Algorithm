
n=int(input())
arr=list(map(int,input().split()))
dp=[1001]*n

if n==1:
    print(0)

else:
    dp[0]=0
    for i in range(n):
        step=arr[i]
        for s in range(1,step+1):
            if i+s<n:
                dp[i+s]=min(dp[i]+1,dp[i+s])
                #print(dp)
    if dp[n-1]==1001:
        print(-1)
    else:
        print(dp[n-1])