import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


room=[]
for _ in range(5):
    room.append(list(input().strip()))
dirs=[(-1,0),(0,1),(1,0),(0,-1)]
res=0



def check(selected):
    visited=set()
    def dfs(x,y):
        visited.add((x,y))
        for dx,dy in dirs:
            nx,ny=x+dx,y+dy
            if (nx,ny) in selected and (nx,ny) not in visited:
                dfs(nx,ny)

    dfs(selected[0][0],selected[0][1])
    
    if len(visited)==7:
        return True
    else:
        return False
    


def dfs_comb(start,depth,s_count,selected):
    global res

    if depth==7:
        if s_count>=4 and check(selected):
            res+=1
        return

    for i in range(start,25):
        x,y=i//5,i%5
        if room[x][y]=="S":
            plus=1
        else:
            plus=0



        dfs_comb(i+1,depth+1,s_count+plus,selected+[(x,y)])




dfs_comb(0,0,0,[])
print(res)