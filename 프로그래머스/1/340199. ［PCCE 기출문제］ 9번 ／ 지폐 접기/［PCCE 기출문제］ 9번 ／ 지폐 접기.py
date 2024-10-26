


def solution(wallet, bill):
    answer = 0
    #지폐의 가로, 세로 비교하기
    
    while True:
        if min(bill)>min(wallet) or max(bill)>max(wallet):
        
            #0이큰경우
            if bill[0]>bill[1]:
                bill[0]=bill[0]//2
            #1이 큰경우
            else:
                bill[1]=bill[1]//2
            
            answer+=1
        else:
            break
    
    return answer