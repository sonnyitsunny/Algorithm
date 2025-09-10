import sys
input = sys.stdin.readline

result=[]
N=int(input())
maps=[]
for _ in range(N):
    maps.append(list(map(int,input().split())))

def move(board, dir):
    N = len(board)
    new = [row[:] for row in board]

    def merge_line(line):
        # 0 제거
        tiles = [x for x in line if x != 0]
        merged = []
        i = 0
        while i < len(tiles):
            # 인접 동일이면 '한 번만' 합치고 두 칸 점프
            if i+1 < len(tiles) and tiles[i] == tiles[i+1]:
                merged.append(tiles[i] * 2)
                i += 2
            else:
                merged.append(tiles[i])
                i += 1
        # 0 패딩
        merged += [0] * (N - len(merged))
        return merged

    if dir == 2:  # 좌
        for i in range(N):
            new[i] = merge_line(new[i])

    elif dir == 3:  # 우
        for i in range(N):
            row = new[i][::-1]
            row = merge_line(row)
            new[i] = row[::-1]

    elif dir == 0:  # 상
        for j in range(N):
            col = [new[i][j] for i in range(N)]
            col2 = merge_line(col)
            for i in range(N):
                new[i][j] = col2[i]

    elif dir == 1:  # 하
        for j in range(N):
            col = [new[i][j] for i in range(N)][::-1]
            col2 = merge_line(col)[::-1]
            for i in range(N):
                new[i][j] = col2[i]

    return new


def backtrack(board,dir,cnt):
    if cnt==5:
        max_v=2
        for i in range(N):
            for j in range(N):
                max_v=max(board[i][j],max_v)
        #print(board)
        result.append(max_v)
        return
    
    
    
    #옮기기
    board=move(board,dir)
    
    
    #상하좌우 0 1 2 3 순으로

    #상
    backtrack(board,0,cnt+1)
    #하
    backtrack(board,1,cnt+1)
    #좌
    backtrack(board,2,cnt+1)
    #우
    backtrack(board,3,cnt+1)

for i in range(4):
    backtrack(maps,i,0)

#print(result)
print(max(result))

