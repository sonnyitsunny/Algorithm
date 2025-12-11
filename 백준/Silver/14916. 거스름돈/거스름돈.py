import sys
input = sys.stdin.readline

N=int(input())
five=N//5
while True:
    

    if (N-five*5)%2==0:
        print(five+(N-five*5)//2)
        break
    else:
        five-=1
        if five<0:
            print(-1)
            break