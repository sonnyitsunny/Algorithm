import sys
input = sys.stdin.readline

n=int(input())
distance=list(map(int,input().split()))
price=list(map(int,input().split()))

cur_price=price[0]
total_cost=cur_price*distance[0]

for i in range(1,n-1):
    if cur_price<=price[i]:
        total_cost+=cur_price*distance[i]

    #이전보다 지금이 더 싼 경우
    else:
        cur_price=price[i]
        total_cost+=cur_price*distance[i]
print(total_cost)
