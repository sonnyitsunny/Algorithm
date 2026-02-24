T=int(input())
for _ in range(T):
    N=int(input())
    price=list(map(int,input().split()))

    money=0
    top_price=price[-1]
    for i in range(N-2,-1,-1):
        if top_price>price[i]:
            money+=top_price-price[i]
        else:
            top_price=price[i]
    print(money)