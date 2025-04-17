#행이 짝수인 경우  열이 짝수인 곳이 하얀칸
#행이 홀수인 경우 열이 홀수 인 곳이 하얀칸


maps=[]

for _ in range(8):
    maps.append(list(input()))

cnt=0
for i in range(8):
    for j in range(8):
        if i%2==0 and j%2==0 and maps[i][j]=='F':
            cnt+=1
        elif i%2==1 and j%2==1 and maps[i][j]=='F':
            cnt+=1

print(cnt)