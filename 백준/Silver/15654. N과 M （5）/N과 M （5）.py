from collections import deque
import sys

from itertools import permutations

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m=map(int,input().split())
numbers=list(map(int,input().split()))


num=list(permutations(numbers,m))
#print(num)
num.sort()

for i in num:
    for j in range(len(i)):
        print(i[j],end=' ')

    print()






# def backtrack(start, path):
#     if len(path) == m:
#         print(*path)
#         return
    
#     for i in range(start,n):
#             backtrack(i,path+[i])

# backtrack(0,[])