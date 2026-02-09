
n = int(input())
arr=list(map(int,input().split()))

cnt=0
arrows=[0]*(1_000_000+1)

for a in arr:
    if arrows[a]>0:
        arrows[a]-=1
        arrows[a-1]+=1
    else:
        cnt+=1
        arrows[a-1]+=1
print(cnt)