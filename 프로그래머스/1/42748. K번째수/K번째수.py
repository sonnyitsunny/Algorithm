def solution(array, commands):
    answer = []
    
    #컨멘드로 반복문 돌리고
    #어레이 끊어냄i-1부터 j-1인덱스까지, 정렬 그리고 k-1인덱스를 answer에 넣어줌
    for command in commands:
        
        temp=[]
        i=command[0]-1
        j=command[1]-1
        k=command[2]-1
        temp=array[i:j+1]
        temp.sort()
        answer.append(temp[k])
    return answer