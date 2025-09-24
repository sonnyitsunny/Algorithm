import sys
input = sys.stdin.readline


N=int(input())

arr=[]

for _ in range(N):
    a,b,c,d=map(int,input().split())
    arr.append((a,b,c,d))

arr.sort(key=lambda x:(x[0],x[1],-x[2],-x[3]))

#시작
start=(3,1)
#~종료
end=(11,30)

cnt=0
id=0
max_end=(0,0)


while start<=end:
    found=False
    while id < N and (arr[id][0],arr[id][1])<=start:
        
        if (arr[id][2],arr[id][3])>max_end:
            max_end=(arr[id][2],arr[id][3])
        
        id+=1
        found=True
    
    if not found:
        cnt=0
        break

    cnt+=1
    start=max_end

    if start>end:
        break


if cnt==0:
    print(0)
else:
    print(cnt)