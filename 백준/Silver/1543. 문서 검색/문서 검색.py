# 어떤 단어가 총 몇 번 등장하는지 세려고 한다
# 중복되어 세는 것은 빼고 세야 한다


book=input()
word=input()

cnt=0
i=0
end=len(word)

while True:
    if i+end<=len(book): # 슬라이싱은 i_end까지 포함하지 않으므로 len(book) - 1이 아니라 len(book)로
        if book[i:i+end]!=word:
            i=i+1
        else:
            cnt+=1
            #print(book[i:i+end])
            i=i+end
            
    else:   
        break
        

print(cnt)