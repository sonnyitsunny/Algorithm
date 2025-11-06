import sys
input = sys.stdin.readline


N=int(input())
arr=list(map(int,input().split()))

left=0
right=N-1
res=abs(arr[left]+arr[right])
pair=(arr[left],arr[right])

while left<right:
    tmp=arr[left]+arr[right]
    if abs(tmp)<res:
        pair=(arr[left],arr[right])
        res=abs(tmp)
    
    if tmp<0:
        left+=1
    elif tmp>0:
        right-=1
    else:
        break
print(pair[0],pair[1])
