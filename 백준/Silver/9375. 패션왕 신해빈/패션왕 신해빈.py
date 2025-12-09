import sys
input = sys.stdin.readline
from collections import defaultdict
N = int(input())

for _ in range(N):
    cloth=defaultdict(int)
    M=int(input())
    for _ in range(M):
        name,category=input().split()
        cloth[category]+=1

    res=1
    for k,v in cloth.items():
        res*=(v+1)
    print(res-1)