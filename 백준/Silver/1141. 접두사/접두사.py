import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
    arr.append(input().strip())

arr.sort(key=lambda x: len(x))
#print(arr)
res=set()
for i in range(n):
    head=arr[i]
    head_len=len(head)
    safe=True
    for j in range(i+1,n):
        
        if head == arr[j][:head_len]:
            
            safe=False
            

    if safe:
        res.add(head)
print(len(res))