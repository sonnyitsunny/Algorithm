
string=input()

exp=input()
n=len(exp)


stack=[]

for s in string:
    stack.append(s)

    if ''.join(stack[-n:]) == exp:
        for _ in range(n):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')