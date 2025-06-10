import sys
input=sys.stdin.readline
n=int(input().strip())
m=int(input().strip())
s=input().strip()

res=0
i=0
tmp=0
while i<(m-1):
    if s[i:i+3]=='IOI':
        i+=2
        tmp+=1
        if tmp==n:
            res+=1
            tmp-=1
    else:
        i+=1
        tmp=0
print(res)