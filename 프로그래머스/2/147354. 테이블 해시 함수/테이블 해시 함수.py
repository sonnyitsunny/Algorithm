def solution(data, col, row_begin, row_end):
   
    data.sort(key=lambda x:(x[col-1],-x[0]))
    
    n=len(data)
    col_len=len(data[0])
    res=[]
    
    for i in range(row_begin-1,row_end):
        tmp=0
        for j in range(col_len):
            tmp+=data[i][j]%(i+1)
        res.append(tmp)
    #print(*res)
    start=res[0]
    
    for r in res[1:]:
        start=start^r
    
    
    
    return start