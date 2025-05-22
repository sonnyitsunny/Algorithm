def solution(brown, yellow):
    answer = []
    cand=[]
    #가로가 m, 세로가 n 
    #가로 1인덱스 ~ m-2인덱스
    #세로 1인덱스 ~ n-2 인덱스까지 다 채워넣는게 옐로우 갯수와 딱 맞고 그 옐로우 갯수+갈색 수 가 m*n이면 그걸 반환
    blocks=brown+yellow
    
    for i in range(2,blocks//2):
        if blocks%i==0:
            cand.append((blocks//i,i))
    
    for m,n in cand:
        if (m-2)*(n-2)==yellow:
            answer.append(m)
            answer.append(n)
            break

    
    
    
    return answer