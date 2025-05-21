import sys
input=sys.stdin.readline

n=int(input())

arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))

arr1.sort()
arr2.sort(reverse=True)
total=0

for i in range(n):
    total+=arr1[i]*arr2[i]
print(total)