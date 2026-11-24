import sys
input = sys.stdin.readline
from collections import Counter

arr=[]
N=int(input())

for _ in range(N):
    arr.append(int(input()))

s=sum(arr)/N # 산순평균
m=s-int(s) # 소수점 부분
if s>0:
    if m>=0.5:
        s=int(s)+1
    else:
        s=int(s)
elif s<0:
    if abs(m)>=0.5:
        s=int(s)-1
    else:
        s=int(s)
else:
    s=0

print(s)
arr.sort()
print(arr[(N//2)])

cnt=Counter(arr)
cnt=sorted(cnt.items(),key=lambda x:(-x[1],x[0]))

if len(cnt)>1:
    if cnt[0][1]==cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])



print(abs(max(arr)-min(arr)))