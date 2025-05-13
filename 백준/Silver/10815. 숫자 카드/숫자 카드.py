import sys
input=sys.stdin.readline

from bisect import bisect_left,bisect_right


n=int(input())
arr=list(map(int,input().split()))
arr.sort()

m=int(input())
target=list(map(int,input().split()))

result=[]

for num in target:
    l=bisect_left(arr,num)
    r=bisect_right(arr,num)

    if r-l!=0:
        result.append(1)
    else:
        result.append(0)
print(*result)