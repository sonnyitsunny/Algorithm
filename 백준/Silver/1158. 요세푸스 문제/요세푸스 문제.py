import sys
input=sys.stdin.readline

n, kill = map(int,(input().split()))

person=[]
result=[]
for i in range(0,n):
    
    person.append(i+1)

while person:
        kill_idx= (kill-1)%len(person)
        result.append(person[kill_idx])
        person.remove(person[kill_idx])
        person=person[kill_idx:]+person[0:kill_idx]

print('<',end='')
for i in range(0,len(result)-1):
      
    print(result[i],end=', ')
print(result[-1],end='')
print('>',end='')