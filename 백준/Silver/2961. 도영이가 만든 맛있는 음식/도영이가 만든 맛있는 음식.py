import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N=int(input())
food=[]
for _ in range(N):
    S,B=map(int,input().split())
    food.append((S,B))


tasty=1e12
def dfs(id,S,B):
    global tasty


    if N==id:
        if not (S==1 and B==0):
            tasty=min(tasty,abs(S-B))
            #print(tasty)
        return
    
    
    dfs(id+1,S*food[id][0],B+food[id][1])
    dfs(id+1,S,B)



dfs(0,1,0)
print(tasty)