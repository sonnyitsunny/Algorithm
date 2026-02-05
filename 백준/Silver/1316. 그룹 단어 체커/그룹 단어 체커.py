n=int(input())
ans=n

for _ in range(n):
    words=list(input())
    already=set()
    prev=words[0]
    
    for w in words[1:]:
        if prev==w and w not in already:
            continue
        #다른 경우
        else:
            if w not in already:
                already.add(prev)
                prev=w
            else:
                ans-=1
                break
                
print(ans)