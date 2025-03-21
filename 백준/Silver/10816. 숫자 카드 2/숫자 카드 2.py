from collections import deque
import sys
from bisect import bisect_left,bisect_right
#가진 카드를 정렬 후 
#M번 반복문을 돌면서 찾아야하는 수를 이분탐색을 통해서 찾고 그과정에선 인덱스계산을해서 갯수를 셈
#그리고 그걸 리스트에 넣음

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
    result.append(right-left)

print(*result)