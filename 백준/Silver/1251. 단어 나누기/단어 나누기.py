word=input()
n=len(word)
tmp=[]

for i in range(1,n-1):
    for j in range(i+1,n):
        word1=word[:i][::-1]
        word2=word[i:j][::-1]
        word3=word[j:][::-1]
        new_word=word1+word2+word3
        tmp.append(new_word)
tmp.sort()
print(tmp[0])