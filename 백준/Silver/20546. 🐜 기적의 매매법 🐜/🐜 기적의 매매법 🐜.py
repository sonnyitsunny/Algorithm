money=int(input())
stock=list(map(int,input().split()))

last=stock[13]

j_money=money
j_cnt=0

s_money=money
s_cnt=0

for s in stock:
    j_cnt+=j_money//s
    j_money=j_money%s

j_total=j_money+j_cnt*last



up_days=0
down_days=0
prev=stock[0]

for s in stock[1:]:
    if s>prev:
        up_days+=1
        down_days=0

    if s<prev:
        down_days+=1
        up_days=0
    
    if up_days>=3:
        
        s_money+=s_cnt*s
        s_cnt=0
    if down_days>=3 and s_money>=s:
        s_cnt+=s_money//s
        s_money=s_money%s
    prev=s

s_total=s_money+s_cnt*last

if j_total==s_total:
    print("SAMESAME")
elif j_total>s_total:
    print("BNP")
else:
    print("TIMING")