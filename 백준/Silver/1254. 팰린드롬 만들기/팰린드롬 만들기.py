import sys
input=sys.stdin.readline


# 원본 문자열 = 뒤집은 문자열인 경우 종료
#원본꺼를 하나씩 떼다 붙인거 + 원본 리버스한거가 원본 리버스와 같다면

words=input().strip()
p_words=words[::-1]
tmp=''

    
      
if words==p_words:
    print(len(words))
else:
    for i in range(len(words)):
        tmp+=words[i]
        if words+tmp[::-1]==tmp+p_words:
            print(len(tmp)+len(words))
            break


