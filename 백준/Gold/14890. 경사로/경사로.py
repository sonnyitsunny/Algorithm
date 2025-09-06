import sys
input = sys.stdin.readline


N,L=map(int,input().split())

maps=[]
for _ in range(N):
    maps.append(list(map(int,input().split())))

#L은 고정길이로 주어짐
#경사로 높이는 1
#모두 같은 높이 이거나, 경사로를 놓아서 길을 지나갈 수 있어야함


def can_pass(line,L):
    n=len(line)
    used=[False]*n

    for j in range(n-1):
        diff=line[j+1]-line[j]

        if diff==0:
            continue
        
        # 오르막 
        if diff==1:
            h=line[j]

            if j-(L-1)<0:
                return False
            
            for k in range(j,j-L,-1):
                if line[k]!=h or used[k]:
                    return False 
            
            for k in range(j,j-L,-1):
                used[k]=True


        # 내리막
        elif diff==-1:
            h=line[j+1]

            if j+L>=n:
                return False

            for k in range(j+1,j+1+L):
                if line[k]!=h or used[k]:
                    return False
            
            for k in range(j+1,j+1+L):
                used[k]=True

        else:
            return False

    return True

cnt=0

#가로
for i in range(N):
    if can_pass(maps[i],L):
        cnt+=1



#세로
for j in range(N):
    col=[maps[i][j] for i in range(N)]
    if can_pass(col,L):
        cnt+=1
print(cnt)