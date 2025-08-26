

import sys
input = sys.stdin.readline

N,M=map(int,input().split())
d={}

for _ in range(N):
    id,pw = input().split()
    d[id]=pw

for _ in range(M):
    id=input().strip()
    print(d[id])

