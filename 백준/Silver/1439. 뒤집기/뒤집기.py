word=input()

count0=0
count1=0

if word[0]=='1':
    count1+=1
else:
    count0+=1


for i in range(1,len(word)):
    if word[i]!=word[i-1]:
        if word[i]=='1':
            count1+=1
        else:
            count0+=1



print(min(count0,count1))

