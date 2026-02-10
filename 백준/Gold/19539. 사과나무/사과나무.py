n=int(input())
h=list(map(int,input().split()))



S=sum(h)
if (S%3)!=0:
    print("NO")
    exit()

C=(S//3)
cnt_2=0

for x in h:
    cnt_2+=(x//2)

if cnt_2>=C:
    print("YES")

else:
    print("NO")
