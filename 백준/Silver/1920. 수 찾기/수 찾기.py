from collections import deque
import sys
from bisect import bisect_left,bisect_right


sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N=int(input())
numbers=list(map(int,input().split()))
numbers.sort()
M=int(input())
target=list(map(int,input().split()))

result=[]

# def binary_search(array,target,start,end):
#     if start>end:
#         return None
#     mid=(start+end)//2

#     if array[mid]==target:
#         return 
#     elif array[mid]>target:
#         return binary_search(array,target,start,mid-1)
#     else:
#         return binary_search(array,target,mid+1,end)
    

for i in range(M):
    left=bisect_left(numbers,target[i])
    right=bisect_right(numbers,target[i])
    if right-left>0:

        result.append(1)
    else:
        result.append(0)

for i in range(M):
    print(result[i])