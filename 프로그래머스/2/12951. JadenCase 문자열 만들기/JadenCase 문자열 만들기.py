def solution(s):
    answer = ''
    #s를 하나하나 다 확인한다.
    #safe=True로 놓고 True일 때만 그 글자의 숫자,글자 여부를 따진다
        #숫자면 그냥 더하고 safe가 False인동안 계속 소문자만 더함
        #글자를 만나면 대문자로 바꾸고더하고 safe False로 바꾸고 계속 소문자만 더함
    #글자를 만나면 safe를 False로 바꾼다.
    #공백을 만나게 된다면 safe를 True로 바꾸고
    
    safe=True
    
    for i in s:
        #단어 맨 앞인 경우
        if safe:
            #글자인경우
            if i.isalpha():
                answer+=i.upper()
                safe=False
            #숫자인경우
            elif i.isdigit() :
                answer+=i
                safe=False
            #공백인경우
            elif i==" ":
                answer+=i
                safe=True
        
        #맨앞이 아닌 경우
        else:
            #글자인 경우
            if i.isalpha():
                answer+=i.lower()
            #공백인경우
            else:
                answer+=i
                safe=True
            
    
    return answer