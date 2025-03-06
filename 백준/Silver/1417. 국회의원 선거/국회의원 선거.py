n=int(input())

if n == 1:
    print(0)
    exit()

num=[]
result=0

for _ in range(0,n):
    m=int(input())
    num.append(m)

main=num[0]
target=num[1:]
while(max(target) >= main):
    p_x=max(target)
    p_i=target.index(p_x)
    target[p_i]-=1
    main+=1
    result+=1


if main in target:
    print(result+1)
else:
    print(result)
