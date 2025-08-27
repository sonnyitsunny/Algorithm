import sys
input = sys.stdin.readline

n=int(input())
dic={}

for _ in range(n):
    name,check=input().split()

    if check=="enter":
        dic[name]=1
    else:
        dic[name]=0
result=[]
for k,v in dic.items():
    if v==1:
        result.append(k)

result.sort(reverse=True)
for name in result:
    print(name)