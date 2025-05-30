import sys
from collections import deque

input = sys.stdin.readline


n,s=map(int,input().split())
arr=list(map(int,input().split()))
cnt=0
def add(id,total):
    global cnt
    if id==n:
        if total==s:
            cnt+=1
        return
    

    add(id+1,total+arr[id])

    add(id+1,total)


add(0,0)
if s==0:
    cnt-=1

print(cnt)