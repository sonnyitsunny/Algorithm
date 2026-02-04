# 해결한 경우 파란색, 해결하지 못한 경우 빨간색
#연속된 애를 압축
#2 1  1 1 2 1
#b r b r b  r

#b r b r b r   #  b와 r의 수 가 같다. 그럼 b또는 r 개수 +1 이 

# 만약 하나가 더크다 .
#b r b r b 1 + 작은 애 개수 

n = int(input())
color=list(input())

comp=[]

prev=color[0]

for c in color[1:]:
    if c==prev:
        continue
    comp.append(prev)
    prev=c
comp.append(prev)

b_cnt=0
r_cnt=0
for com in comp:
    if com=="B":
        b_cnt+=1
    else:
        r_cnt+=1

ans = min(b_cnt,r_cnt)
print(ans+1)