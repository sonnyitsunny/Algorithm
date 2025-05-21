import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
    x,y=map(int,input().split())
    arr.append((x,y))

arr.sort(key=lambda x: (x[1],x[0]))
cnt=0
start=0
for x,y in arr:
    #직전 종료 시간이 지금 시작 시간보다 작다면
    if start<=x:
        cnt+=1
        start=y
    else:
        continue

print(cnt)