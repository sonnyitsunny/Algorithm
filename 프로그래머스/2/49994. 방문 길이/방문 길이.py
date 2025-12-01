def solution(dirs):
    answer = 0
    x=0
    y=0          # 여기선 그냥 x좌표 , y좌표로 가정하자
    visited=set()
    
    for dir in dirs:
        px=x
        py=y
        if dir=="U" and -5<=y+1<=5:
            y+=1
            if (px,py,x,y) in visited or (x,y,px,py) in visited:
                continue
            visited.add((px,py,x,y))
            visited.add((x,y,px,py))
            answer+=1
            
            
            
        elif dir=="D" and -5<=y-1<=5:
            y-=1
            if (px,py,x,y) in visited or (x,y,px,py) in visited:
                continue
            visited.add((px,py,x,y))
            visited.add((x,y,px,py))
            answer+=1
        elif dir=="R" and -5<=x+1<=5:
            x+=1
            if (px,py,x,y) in visited or (x,y,px,py) in visited:
                continue
            visited.add((px,py,x,y))
            visited.add((x,y,px,py))
            answer+=1
            
        elif dir=="L" and -5<=x-1<=5:
            x-=1
            if (px,py,x,y) in visited or (x,y,px,py) in visited:
                continue
            visited.add((px,py,x,y))
            visited.add((x,y,px,py))
            answer+=1
    #print(visited)
    
    return answer