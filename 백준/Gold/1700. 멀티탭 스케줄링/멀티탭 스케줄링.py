import sys
input = sys.stdin.readline

n,k=map(int,input().split())
arr=list(map(int,input().split()))

plug=set()
change=0


for i in range(k):
    if arr[i] in plug:
        continue
    
    if len(plug)<n:
        plug.add(arr[i])
        continue

    notuse=-1
    target=0

    for p in plug:
        if p not in arr[i+1:]:
            target=p
            break

        else:
            id=arr[i+1:].index(p)+i+1
            if id>notuse:
                notuse=id
                target=p
    plug.remove(target)
    plug.add(arr[i])
    change+=1

print(change)
