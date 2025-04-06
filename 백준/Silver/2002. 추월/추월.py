n=int(input())
#대근
entrance=[]
#영식
exit=[]

cnt=0
wanted={}

for _ in range(n):
    entrance.append(input())

for _ in range(n):
    exit.append(input())

i=0
j=0
while True:
    
    if i+cnt<n:
        
        if entrance[j] in wanted:
            j+=1
            continue

        else:
            if entrance[j]==exit[i+cnt]:
                j+=1
                i+=1

            elif entrance[j]!=exit[i+cnt]:
                wanted[exit[i+cnt]]=1
                cnt+=1
    else:
        break
#print(wanted)
print(cnt)