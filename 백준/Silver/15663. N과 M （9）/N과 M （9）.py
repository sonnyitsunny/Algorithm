from collections import deque
import sys


sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m=map(int,input().split())
numbers=list(map(int,input().split()))

numbers.sort()

visited=[False] * n



def backtrack(path):
    if len(path) == m:
        print(*path)
        return
    
    prev=-1
    
    for i in range(n):
        if not visited[i] and prev!=numbers[i]:
            visited[i]=True
            backtrack(path+[numbers[i]])
            visited[i]=False
            prev=numbers[i]
            
            

backtrack([])