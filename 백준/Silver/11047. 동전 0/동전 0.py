n,k=map(int,input().split())

money=[]
for _ in range(n):
    money.append(int(input()))

leng=len(money)
money.sort(reverse=True)
coin=0
while k!=0:
    for m in money:
        if (k//m)>0:
            coin+=k//m
            k=k-(k//m)*m


print(coin)