from collections import deque
import sys

from itertools import combinations

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m=map(int,input().split())


def backtrack(start, path):
    if len(path) == m:
        print(*path)
        return
    
    for i in range(start,n+1):
            backtrack(i,path+[i])

backtrack(1,[])
