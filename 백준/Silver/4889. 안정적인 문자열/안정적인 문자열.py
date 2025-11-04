import sys
input = sys.stdin.readline




case=1

while True:
    words=input().strip()

    if '-' in words:
        break

    stack=[]
    cnt=0



    for ch in words:
        if ch == "{":
            stack.append(ch)
        else:
            if stack:
                stack.pop()
            else:
                cnt+=1
                stack.append("{")

    cnt+=len(stack)//2
    print(f"{case}. {cnt}")
    case+=1