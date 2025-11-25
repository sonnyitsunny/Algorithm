def solution(arr):
    
    n=len(arr)
    
    def compress(x,y,size):
        safe=True
        first=arr[x][y]
        for i in range(x,x+size):
            for j in range(y,y+size):
                if arr[i][j]!=first:
                    safe=False
                    break
            if not safe:
                break
        if safe:
            if first==0:
                return (1,0)
            else:
                return (0,1)
                
        half=size//2
        z1,o1=compress(x,y,half)
        z2,o2=compress(x+half,y,half)
        z3,o3=compress(x,y+half,half)
        z4,o4=compress(x+half,y+half,half)
        return (z1+z2+z3+z4,o1+o2+o3+o4)
    
    zero,one=compress(0,0,n)
    return [zero,one]