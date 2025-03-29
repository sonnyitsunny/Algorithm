word=input()

n=len(word)

tmp=[]

for i in range(n):
    tmp.append(word[i:])

tmp.sort()
for t in tmp:
    print(t)