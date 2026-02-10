
a1,hp1=map(int,input().split())
a2,hp2=map(int,input().split())

while hp1>0 and hp2>0:
    hp1-=a2
    hp2-=a1
if hp1<=0 and hp2<=0:
    print("DRAW")
    
elif hp1<hp2:
    print("PLAYER B")
elif hp1>hp2 :
    print("PLAYER A")