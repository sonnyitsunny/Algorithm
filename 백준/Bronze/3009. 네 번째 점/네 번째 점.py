
point=[]


nx=[]
ny=[]
for _ in range(3):
    x,y=map(int,input().split())
    nx.append(x)
    ny.append(y)

nx.sort()
ny.sort()

rx=0
ry=0
if nx[0]==nx[1]:
    rx=nx[2]
else:
    rx=nx[0]


if ny[0]==ny[1]:
    ry=ny[2]
else:
    ry=ny[0]

print(rx,ry)