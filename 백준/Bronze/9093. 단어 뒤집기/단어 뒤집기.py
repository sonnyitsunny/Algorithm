t=int(input())

for _ in range(t):
    
    words=list(input().split())
    for word in words:
        print(word[::-1],end=' ')
    print()
