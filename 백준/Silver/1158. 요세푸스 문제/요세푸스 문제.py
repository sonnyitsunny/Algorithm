N,K=map(int,input().split())

bef = []
res=[]



for i in range(N):
    bef.append(i+1)

t_idx=K-1

while len(res)!=N:
    t_idx=t_idx%len(bef)
    
    res.append(bef.pop(t_idx))
        
    t_idx=t_idx+K-1




print("<"+", ".join(map(str,res))+">")