import sys
input = sys.stdin.readline

word=input().strip()
n=int(input())

res=0
for _ in range(n):
    target=input().strip()
    target=target+target
    if word in target:
        res+=1
print(res)