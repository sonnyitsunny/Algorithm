n=int(input())

for _ in range(n):
    c=int(input())

    maps=[]
    dp=[[0]*c for _ in range(2)]
    for _ in range(2):
        maps.append(list(map(int,input().split())))
    if c==1:
        print(max(maps[0][0],maps[1][0]))
        continue



    dp[0][0]=maps[0][0]
    dp[1][0]=maps[1][0]

    dp[0][1]=dp[1][0]+maps[0][1]
    dp[1][1]=dp[0][0]+maps[1][1]


    for i in range(2,c):
        
        dp[0][i]=maps[0][i]+max(dp[1][i-1],dp[1][i-2])
        dp[1][i]=maps[1][i]+max(dp[0][i-1],dp[0][i-2])
    
    
    print(max(dp[0][c-1],dp[1][c-1]))