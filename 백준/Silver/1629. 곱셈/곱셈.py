import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

a,b,c=map(int,input().split())


def pow(a,b,c):
    if b==1:
        return a%c
    half = pow(a,b//2,c)

    if b%2==0:
        return (half * half) % c
    else:
        return (half*half*a)%c



print(pow(a,b,c))