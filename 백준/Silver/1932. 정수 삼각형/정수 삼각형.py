n=int(input())

t=[]
for _ in range(n):
    t.append(list(map(int,input().split())))

for i in range(n-2,-1,-1):
    for j in range(len(t[i])):
        t[i][j]+=max(t[i+1][j],t[i+1][j+1])

print(t[0][0])