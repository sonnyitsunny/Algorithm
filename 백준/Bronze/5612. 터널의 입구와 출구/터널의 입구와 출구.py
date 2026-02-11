n=int(input())
prev_tunnel=int(input())
res=[prev_tunnel]
for _ in range(n):
    ent,exi=map(int,input().split())
    prev_tunnel=ent+prev_tunnel-exi
    res.append(prev_tunnel)
if min(res)<0:
    print(0)
else:
    print(max(res))