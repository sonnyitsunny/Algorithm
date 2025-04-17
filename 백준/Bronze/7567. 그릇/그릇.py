dish=list(input())

height=0

tmp=dish[0]
height=10

for i in range(1,len(dish)):
    if dish[i]!=tmp:
        height+=10
        tmp=dish[i]
    else:
        height+=5
print(height)