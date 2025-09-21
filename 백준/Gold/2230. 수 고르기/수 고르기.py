import sys


input = sys.stdin.readline

N,M=map(int,input().split())
arr=[]
for _ in range(N):
    arr.append(int(input()))

ans=float('inf')
arr.sort()

left=0
right=1

while left < N and right<N:
    diff=arr[right]-arr[left]
    if diff<M:
        right+=1
    else:
        ans=min(ans,diff)
        left+=1

print(ans)