import sys
input = sys.stdin.readline
from itertools import permutations

n=int(input())

nums=permutations(range(1,n+1))

sorted_nums=sorted(nums,key=lambda x:sum(x))


for num in sorted_nums:
    for i in range(len(num)):
        print(num[i],end=' ')
    print()
