import sys
input = sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
    x,y=map(int,input().split())
    arr.append((x,y))


arr.sort(key=lambda x:(x[0],-x[-1]))

length=0

x,y=arr[0]
length+=y-x
right=y



for i in range(1,n):

    if arr[i][0]<right:
        if arr[i][1]>right:
            length+=arr[i][1]-right
            right=arr[i][1]

        else:
            continue
    
    else:
        length+=arr[i][1]-arr[i][0]
        right=arr[i][1]
print(length)