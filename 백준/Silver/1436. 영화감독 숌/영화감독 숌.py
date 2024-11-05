#종말의 수란 어떤 수에 6이 적어도 3개 이상 연속으로 들어가는 수

N=int(input())

count=0
target=666
while True:
    if '666' in str(target):
        count+=1
        
        if N==count:
            print(target)
            break
        
    
    target+=1
        