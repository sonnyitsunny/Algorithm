# | 합집합, & 교집합 <- 그냥 집합인 경우
# 첨에 받자마자 다 소문자 처리한다.  b=a.lower()

# 다 2글자씩 나눈다
# A와 B 중에 다중집합이 있는지 확인한다.
#없다면 그냥 자카드 유사도, 있면 다중집합으로 자카드 유사도

from collections import Counter
def solution(str1, str2):
    answer = 0
    str1=str1.lower()
    str2=str2.lower()
    n1=len(str1)
    n2=len(str2)
    tmp1=[]
    tmp2=[]
    
    alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    for i in range(n1-1):
        if str1[i] in alpha and str1[i+1] in alpha:
            tmp1.append(str1[i]+str1[i+1])
    for i in range(n2-1):
        if str2[i] in alpha and str2[i+1] in alpha:
            tmp2.append(str2[i]+str2[i+1])
        
        
        
    if len(set(tmp1)|set(tmp2))==0:
        return 65536
        
        
        
    if len(tmp1) == len(set(tmp1)) and len(tmp2) == len(set(tmp2)):
        
        answer=int(len(set(tmp1)&set(tmp2))/len(set(tmp1)|set(tmp2))*65536)         
        return answer
    

    else:
        c1=Counter(tmp1)
        c2=Counter(tmp2)
        
        target1=set()
        target2=set()
        res1=[]
        res2=[]
        #교집합 
        for k in set(tmp1):
            if k in tmp2 and k not in target1:
                target1.add(k)
                cnt=min(c1[k],c2[k])
                for _ in range(cnt):
                    res1.append(k)
        #합집합
        for k in set(tmp1):
            if k in tmp2 and k not in target2:
                target2.add(k)
                cnt=max(c1[k],c2[k])
                for _ in range(cnt):
                    res2.append(k)
            elif k not in tmp2 and k not in target2:
                target2.add(k)
                for _ in range(c1[k]):
                    res2.append(k)
                
        
        
        for k in set(tmp2):
            if k not in target2:
                for _ in range(c2[k]):
                    res2.append(k)
        
        
     
        answer=int(len(res1)/len(res2)*65536)
        return answer
        
        
        
        
        
        
        
        
        
        
        
        