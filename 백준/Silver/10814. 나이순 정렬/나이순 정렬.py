from collections import deque
import sys
from bisect import bisect_left,bisect_right


sys.setrecursionlimit(10**6)
input = sys.stdin.readline
info=[]
N=int(input())
for i in range(N):
    age,name=input().split()
    info.append((int(i),int(age),name))


info.sort(key=lambda x:(x[1],x[0]))

for person in info:
    print(person[1],person[2])