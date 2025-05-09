n = int(input())

dic={1:1,2:2}



for i in range(3, 1001):
    dic[i] = dic[i-1]+dic[i-2]
    
   


print(dic[n]%10007)
    
    

