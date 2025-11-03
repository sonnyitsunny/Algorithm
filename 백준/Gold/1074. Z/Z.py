import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline






def z(n,r,c):
    if n==0:
        return 0
    half=2**(n-1)
    size=half*half

    if r<half and c<half:
        return z(n-1,r,c)
    elif r<half and half<=c:
        return size*1+z(n-1,r,c-half)
    elif half<=r and c<half:
        return 2*size+z(n-1,r-half,c)
    elif half<=r and half<=c:
        return 3*size+z(n-1,r-half,c-half)
        


N,r,c=map(int,input().split())
print(z(N,r,c))