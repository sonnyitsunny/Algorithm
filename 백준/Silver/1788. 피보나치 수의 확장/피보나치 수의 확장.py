import sys
input = sys.stdin.readline

n=int(input())


sign=0


if n==0:
    print(0)
    print(0)
else:
    k=abs(n)
    dp=[0]*(k+1)
    dp[1]=1

    for i in range(2,k+1):
        dp[i]=(dp[i-1]+dp[i-2])%1_000_000_000

    if n>0:
        sign=1

    else:
        if n%2==0:
            sign=-1
        

        else:
            sign=1

    print(sign)
    print(dp[k])