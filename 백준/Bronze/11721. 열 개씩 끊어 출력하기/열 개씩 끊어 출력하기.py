words=input()

cnt=len(words)//10

m=len(words)%10


for i in range(cnt):
    s=i*10

    print(words[s:s+10])

if m>0:
    print(words[cnt*10:])