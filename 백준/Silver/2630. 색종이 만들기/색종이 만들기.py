import sys
input = sys.stdin.readline

N=int(input())
arr=[]
for _ in range(N):
    arr.append(list(map(int,input().split())))

def make(x,y,size):
    first=arr[x][y]
    safe=True
    for i in range(x,x+size):
        for j in range(y,y+size):
            if arr[i][j]!=first:
                safe=False
                break
        if not safe:
            break
    if safe:
        if first==0: #하얀색
            return 1,0
        else:
            return 0,1


    half=size//2
    w1,b1=make(x,y,half)
    w2,b2=make(x+half,y,half)
    w3,b3=make(x,y+half,half)
    w4,b4=make(x+half,y+half,half)

    return w1+w2+w3+w4,b1+b2+b3+b4



white,blue=make(0,0,N)
print(white)
print(blue)