from collections import deque
import sys

from itertools import combinations

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m=map(int,input().split())



numbers=list(combinations(range(1,n+1),m))

for num in numbers:
    
    for i in range(0,len(num)):
        print(num[i],'',end='')
    print()
       
