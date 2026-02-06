#배열로 받고 reverse해서 감소하는 배열로 
n=int(input())

arr=[]
cnt=0

for _ in range(n):
    arr.append(int(input()))
arr.reverse()

for i in range(n-1):
    if arr[i]>arr[i+1]:
        continue
    diff=arr[i+1]-arr[i]
    arr[i+1]=arr[i]-1
    cnt+=diff+1

print(cnt)