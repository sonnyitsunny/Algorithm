import sys
input = sys.stdin.readline

T=int(input())

for _ in range(T):
    arr=[]
    N=int(input())
    for _ in range(N):
        a,b=map(int,input().split())
        arr.append((a,b))
    arr.sort(key=lambda x:x[0])

    best=100001
    cnt=0

    for _, interview in arr:
        if interview<best:
            cnt+=1
            best=interview
    print(cnt)