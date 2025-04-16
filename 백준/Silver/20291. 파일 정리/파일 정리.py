n=int(input())

hash={}
for _ in range(n):
    word,extend=input().split('.')

    if extend in hash:
        hash[extend]+=1
    else:
        hash[extend]=1
sorted_hash=sorted(hash.items(),key=lambda x:x[0])
for k,v in sorted_hash:
    print(k,v)