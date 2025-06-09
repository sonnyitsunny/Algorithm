from itertools import permutations

n=int(input())

q=[]

for _ in range(n):
    num,s,b=input().split()
    q.append((num,int(s),int(b)))

cnt=0
can=list(permutations(range(1,10),3))
for c in can:
    c_str=''.join(map(str,c))
    safe=True
    for q_num,q_s,q_b in q:
        strike=0
        ball=0

        for i in range(3):
            if c_str[i]==q_num[i]:
                strike+=1
            elif c_str[i] in q_num:
                ball+=1
        
        if strike!=q_s or ball!=q_b:
            safe=False
            break
        
    if safe:
        cnt+=1
print(cnt)