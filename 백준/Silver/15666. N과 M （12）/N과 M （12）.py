from collections import deque
import sys


sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m=map(int,input().split())
numbers=list(map(int,input().split()))

numbers.sort()

visited=[False] * n



def backtrack(start,path):
    if len(path) == m:
        print(*path)
        return
    
    prev=-1
    
    for i in range(start,n):
        if  prev!=numbers[i]:
            
            backtrack(i,path+[numbers[i]])
            
            prev=numbers[i]
            
            

backtrack(0,[])