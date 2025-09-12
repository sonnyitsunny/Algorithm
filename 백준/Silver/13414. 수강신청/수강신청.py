import sys
input = sys.stdin.readline

waiting={}
K,L=map(int,input().split())

for i in range(1,L+1):
    num=input().strip()
    waiting[num]=i

res=sorted(waiting.items(),key=lambda x:x[1])
#print(res)
for i in range(min(K,len(res))):
    print(res[i][0])