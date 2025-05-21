import sys
input=sys.stdin.readline

n=int(input())


for _ in range(n):
    a,b=input().split()
    arr1=list(a)
    arr2=list(b)
    safe=True
    arr1.sort()
    arr2.sort()
    if len(arr1)!=len(arr2):
        print("Impossible")
        continue

    for i in range(len(arr1)):
        if arr1[i]!=arr2[i]:
            print("Impossible")
            safe=False
            break

    if not safe:
        continue
    print("Possible")
