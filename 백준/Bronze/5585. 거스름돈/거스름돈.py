import sys
input = sys.stdin.readline

T=int(input())

coin=1000-T

cnt=0
while True:
    if coin==0:
        break

    cnt+=coin//500
    coin=coin%500

    cnt+=coin//100
    coin=coin%100

    cnt+=coin//50
    coin=coin%50

    cnt+=coin//10
    coin=coin%10

    cnt+=coin//5
    coin=coin%5

    cnt+=coin//1
    coin=0
print(cnt)