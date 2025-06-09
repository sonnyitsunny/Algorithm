n,k=map(int,input().split())
countries=[]
for _ in range(n):
    data=list(map(int,input().split()))
    countries.append(data)

countries.sort(key=lambda x:(-x[1],-x[2],-x[3]))

rank=1
prev=countries[0][1:]
ranks={}
ranks[countries[0][0]]=rank

for i in range(1,n):
    now=countries[i][1:]

    if now==prev:
        ranks[countries[i][0]]=rank
    else:
        rank=i+1
        ranks[countries[i][0]]=rank
        prev=now
print(ranks[k])