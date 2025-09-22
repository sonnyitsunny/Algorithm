import sys
input = sys.stdin.readline

T=int(input())

for _ in range(T):
    N=int(input())
    days=list(map(int,input().split()))
    money=0

    best=days[-1]

    for i in range(N-2,-1,-1):
        if best>days[i]:
            money+=best-days[i]
        else:
            best=days[i]
       #print(best,days[i])
    print(money)