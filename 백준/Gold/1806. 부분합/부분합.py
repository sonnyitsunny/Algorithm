import sys
input = sys.stdin.readline

N,S=map(int,input().split())
arr=list(map(int,input().split()))

left=0
right=0

answer=N+1
res=arr[left]

while True:

    if res>=S:

        answer=min(answer,right-left+1)
        res-=arr[left]
        left+=1
        
    else:
        if right<N-1:
            right+=1
            res+=arr[right]
        else:
            break


        
    
       

if answer==N+1:
    print(0)
else:
    print(answer)

