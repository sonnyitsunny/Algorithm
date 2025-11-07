import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right


T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

A_sub = []
B_sub = []

for i in range(n):
    s = 0
    for j in range(i, n):
        s += A[j]
        A_sub.append(s)

for i in range(m):
    s = 0
    for j in range(i, m):
        s += B[j]
        B_sub.append(s)

A_sub.sort()
B_sub.sort()
ans=0
for a in A_sub:
    target = T - a
    l = bisect_left(B_sub, target)
    r = bisect_right(B_sub, target)
    ans += (r - l)
print(ans)