import sys
input = sys.stdin.readline

T=int(input())

n=0
cur=1

while T>=cur:
    T-=cur
    n+=1
    cur+=1
print(n)