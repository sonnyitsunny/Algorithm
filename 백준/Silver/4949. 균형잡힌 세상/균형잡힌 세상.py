#while문을 .가 들어올 때까지 돈다.
#Input을 리스트에 넣어서 for문 돌린다
#포문 돌리면서 () [] 를 하나의 스택에 넣는다.
# 괄호가 하나도 없는 경우 yes
#스택에서 ) 와 ]만 직전에 같은 짝이 있는지 확인한다. 마지막에 스택이 비어있으면 yes 남아있거나 중간에 짝이 안맞으면 바로 no


while True:
    stack=[]
    
    n=input()

    if n=='.':
        break
    
    elif '[' not in n and ']' not in n and '(' not in n and ')' not in n:
        print('yes')

    else:
        words=list(n)
        #print(words)
        
        for i in words:
            
            if i == '(' or i=='[':
                stack.append(i)
            #스택이 비어있는 경우는 그냥 바로 no
            elif i==')':
                if len(stack)==0 or stack[-1]!='(':
                    stack.append(i)
                    break

                else:
                    stack.pop()

            elif i==']':
                if len(stack)==0 or stack[-1]!='[':
                    stack.append(i)
                    break

                else:
                    stack.pop()
        
        if len(stack)==0:
            print('yes')
        else:
            print('no')