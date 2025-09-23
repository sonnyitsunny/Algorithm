import sys
input = sys.stdin.readline


n,c=map(int,input().split())

m=int(input())
town=[c]*(n+1)
#1base



arr=[]

for _ in range(m):
    start,end,box=map(int,input().split())
    arr.append((start,end,box))
 

arr.sort(key=lambda x:x[1])

total=0
for start,end,box in arr:
    c_take=min(town[start:end])

    take=min(c_take,box)

    for i in range(start,end):
        town[i]-=take
    total+=take
print(total)