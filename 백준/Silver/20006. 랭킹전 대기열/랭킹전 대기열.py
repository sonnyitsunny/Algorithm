

#입력 p번

p,m=map(int,input().split())

rooms=[[] for _ in range(300)]
# print(rooms)

for _ in range(p):
    arr=input().split()
    
    info=(int(arr[0]),arr[1])
    #print(info)
    for i in range(300):
        if 0<len(rooms[i])<m and (rooms[i][0][0]-10<=info[0]<=rooms[i][0][0]+10):
            #print(i)
            rooms[i].append(info)
            break
        elif len(rooms[i])==0:
            rooms[i].append(info)
            break
            
for room in rooms:
    if room:
        room.sort(key=lambda x:x[1])
        if len(room)==m:
            print("Started!")
            for l,n in room:
                print(l,n)
        else:
            print("Waiting!")
            for l,n in room:
                print(l,n)