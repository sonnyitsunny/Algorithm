import sys
input = sys.stdin.readline


n=int(input())

d={}
for _ in range(n):
    word=input().strip()
    
    for i in range(len(word)):
        num=10**(len(word)-i-1)
        if word[i] in d:
            d[word[i]]+=num
        else:
            d[word[i]]=num

sort_d=sorted(d.items(),key=lambda x:-x[1])

ans=0

k=9
for target in sort_d:
    ans+=k*target[1]
    k-=1
print(ans)