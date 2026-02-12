N=int(input())
candy=[list(input()) for _ in range(N)]

def check_max():
    best=1
    for r in range(N):
        cnt=1
        for c in range(N-1):
            if candy[r][c]==candy[r][c+1]:
                cnt+=1
            else:
                cnt=1
            if cnt>best:
                best=cnt
    for c in range(N):
        cnt=1
        for r in range(N-1):
            if candy[r][c]==candy[r+1][c]:
                cnt+=1
            else:
                cnt=1
            if cnt>best:
                best=cnt

    return best

ans=check_max()

for r in range(N):
    for c in range(N):
        if r+1<N and candy[r][c]!=candy[r+1][c]:
            candy[r][c],candy[r+1][c]=candy[r+1][c],candy[r][c]
            ans=max(check_max(),ans)
            candy[r][c],candy[r+1][c]=candy[r+1][c],candy[r][c]
        
        if c+1<N and candy[r][c]!=candy[r][c+1]:
            candy[r][c],candy[r][c+1]=candy[r][c+1],candy[r][c]
            ans=max(check_max(),ans)
            candy[r][c],candy[r][c+1]=candy[r][c+1],candy[r][c]
print(ans)