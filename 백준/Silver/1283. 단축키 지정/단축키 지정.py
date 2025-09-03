import sys
input = sys.stdin.readline


# 단어 맨앞만 확인
# 단어 자체 확인

#여기에는 소문자로 해서 넣어놓자
already=[]
result=[]


n=int(input())

check=True

for _ in range(n):
    check=False
    option=list(input().split())
    

    for i in range(len(option)):
        if (option[i][0]).lower() in already:
            continue
        else:
            already.append(option[i][0].lower())
            option[i]="["+option[i][0]+"]"+option[i][1:]
            check=True
            result.append(' '.join(option))
            break


    # 단어 맨앞 단계에서 등록된 경우
    if check:
        continue

    #맨 앞에서 안나온 경우
    for i in range(len(option)):
        word_len=len(option[i])

        for j in range(1,word_len):
            if (option[i][j]).lower() in already:
                continue
            else:
                already.append(option[i][j].lower())
                option[i]=option[i][:j]+"["+option[i][j]+"]"+option[i][j+1:]
                check=True
                result.append(' '.join(option))
                break
        if check:
            break
    #안되는 경우
    if not check:
        result.append(' '.join(option))
for k in result:
    print(k)