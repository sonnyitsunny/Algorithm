import sys
input = sys.stdin.readline

T=int(input())

for _ in range(T):
    q=0
    d=0
    n=0
    p=0

    C=int(input())
    q=C//25
    C=C%25

    d=C//10
    C=C%10

    n=C//5
    C=C%5

    p=C
    




    print(q,d,n,p)