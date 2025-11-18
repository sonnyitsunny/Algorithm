import sys
input = sys.stdin.readline
from itertools import permutations
n=int(input())
arr=list(map(int,input().split()))

max_cnt=0
for per in permutations(arr):
    cnt=0
    for i in range(len(per)-1):
        cnt+=(abs(per[i]-per[i+1]))

    max_cnt=max(max_cnt,cnt)

print(max_cnt)