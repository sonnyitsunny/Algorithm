

# (몸무게, 키) = 덩치
#몸무게와 키 둘다 커야 덩치가 크다고 할수있다.

N=int(input())

body=[]
for _ in range(N):
    h,w=map(int,input().split())
    body.append((h,w))

res=[]

for i in range(N):
    t_l=body[i][0] # 내 키 
    t_w=body[i][1] # 내 무게

    rank=1
    for j in range(N):
        if i==j:
            continue

        c_l=body[j][0] #비교대상 키 
        c_w=body[j][1] #비교대상 무게
        if c_l >t_l and c_w>t_w:
            rank+=1
    res.append(rank)
print(*res)
