import sys
input = sys.stdin.readline


n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))


ans=0

for i in range(n-1,0,-1):
    
    if arr[i]>arr[i-1]:
        continue

    else:
        plus=arr[i-1]-arr[i]+1
        arr[i-1]=arr[i-1]-plus
        ans+=plus
print(ans)