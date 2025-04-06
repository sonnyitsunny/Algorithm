word=input()
word=list(word)
word.sort(reverse=True)


mod=0

num=''

for i in range(len(word)):
    mod = mod + int(word[i])%3
    num+=word[i]

if mod%3 == 0 and int(num)%30==0:
    print(int(num))
else:
    print(-1)