import sys
input = sys.stdin.readline

from itertools import combinations

#모음
a=set(["a","e","i","o","u"])



L,C=map(int,input().split())

targets=list(input().split())

targets.sort()




for com in combinations(targets,L):
    mo=0
    for ch in com:
        if ch in a:
            mo+=1
    ja=len(com)-mo
    if mo>=1 and ja>=2:
        print(''.join(com))