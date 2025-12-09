import sys
input = sys.stdin.readline
from bisect import bisect_right
N,L=map(int,input().split())
arr=list(map(int,input().split()))

arr.sort()

cnt=0


i=0
while i<=N-1:
  
    target=arr[i]
    left=target-0.5
    right=int(left+L)

    id=bisect_right(arr,right)
    cnt+=1
    i=id
print(cnt)