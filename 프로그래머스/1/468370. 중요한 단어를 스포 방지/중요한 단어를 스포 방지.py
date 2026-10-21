def solution(message, spoiler_ranges):
    answer = 0
    already=set() # 공개, 즉 이미미있는애들
    message_arr=list(message.split())
    arr=[""]*(20001)
    #print(arr)
    start=0
    end=0
    for m in message_arr:
        start = message.find(m, start)
        end=start
        length=len(m)
        end+=length
        end-=1
        
        for i in range(start,start+length):
            arr[i]=m
            #print(m)
        check=True
        for s in spoiler_ranges:
            if end<int(s[0]) or start>int(s[1]):
                continue
            check=False    
            break
        if check:
            already.add(m)
    
        start=end+1
    #print(already)
    for s in spoiler_ranges:
        for i in range(int(s[0]),int(s[1])+1):
            if arr[i]!="" and arr[i] not in already:
                answer+=1
                already.add(arr[i])
            
    print(already)
        
    return answer