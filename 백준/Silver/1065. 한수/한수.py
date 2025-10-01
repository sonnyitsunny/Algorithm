import sys
input = sys.stdin.readline

n=int(input())

if n<100:
    count=n

else:
    count=99

    for i in range(100,n+1):
        s=str(i)
        if int(s[0])-int(s[1])==int(s[1])-int(s[2]):
            count+=1

print(count)