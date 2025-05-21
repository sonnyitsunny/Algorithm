import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
arr=[]
max_ans=0
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)


for i in range(n):
    ans=arr[i]*(i+1)
    max_ans=max(ans,max_ans)
print(max_ans)