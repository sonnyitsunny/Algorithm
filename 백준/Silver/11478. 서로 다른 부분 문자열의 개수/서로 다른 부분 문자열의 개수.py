hash={}
words=input()

for i in range(1,len(words)+1):
    
    for j in range(len(words)):
        if j+i<=len(words):
            
            if not words[j:j+i] in hash:
                hash[words[j:j+i]]=1
            else:
                pass

        else:
            break
print(len(hash))
#print(hash)