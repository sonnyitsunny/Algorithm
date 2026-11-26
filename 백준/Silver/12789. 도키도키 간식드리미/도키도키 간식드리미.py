N=int(input())
arr=list(map(int,input().split()))

arr.reverse()



waiting=[]
number=1
while arr:
    first=arr.pop()
    if waiting:
        w_first=waiting.pop()
        if number==first:
            number+=1
            waiting.append(w_first)
            continue
        elif number == w_first:
            number+=1
            arr.append(first)
            continue
        else:
            waiting.append(w_first)

    if number==first:
        number+=1
        continue


    waiting.append(first)

for i in range(number,N+1):
    if waiting:
        w_first=waiting.pop()
        if i == w_first:
            number+=1
        else:
            
            break

if number==N+1:
    print("Nice")
else:
    print("Sad")
