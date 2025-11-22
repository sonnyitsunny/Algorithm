import sys
input = sys.stdin.readline

import heapq

T=int(input())
arr=[]
cnt=0
for _ in range(T):
    n=int(input())
    arr.append(n)

heapq.heapify(arr)
while True:
    if len(arr)==1:
        break
    n1=heapq.heappop(arr)
    n2=heapq.heappop(arr)
    cnt+=n1+n2
    heapq.heappush(arr,n1+n2)
    
    

print(cnt)