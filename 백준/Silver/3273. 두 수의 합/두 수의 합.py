import sys
input=sys.stdin.readline


n=int(input())
arr=list(map(int,input().split()))
x=int(input())

arr.sort()
l=0
r=n-1
cnt=0

while l<r:
    total=arr[l]+arr[r]

    if total==x:
        cnt+=1
        l+=1
        r-=1
    elif total<x:
        l+=1
    else:
        r-=1
print(cnt)