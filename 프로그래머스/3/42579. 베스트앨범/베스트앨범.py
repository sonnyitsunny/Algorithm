#우선순위
#1 가장 많이 재생된 장르가 1순위(2개) 장르 순으로 정렬 해야할 듯
#2 장르 내에서 많이 재생된 곡이 1순위(2개) 재생 순으로 정렬하고 고유번호 낮은 거 앞에 오도록 정렬


#구현
#장르를 키값으로 하는 딕셔너리 해서 장르별 재생횟수 구하기
#장르를 키값으로 하고 값이 2차원 리스트 [[고유번호,횟수],[고유번호,횟수]] (횟수 순으로 정렬하고 고유번호 증가하는 순으로 정렬)
from collections import defaultdict

def solution(genres, plays):
    answer = []
    cnt=defaultdict(int)
    result=defaultdict(list)
    n=len(genres)
    for i in range(n):
        genre=genres[i]
        play=plays[i]

        cnt[genre]+=play
        result[genre].append([i,play])
        
        
        
    #print(dict(cnt))
    #print(dict(result))
    
    sorted_cnt=sorted(cnt.items(),key=lambda x: -x[1])
    for k,v in result.items():
        v.sort(key=lambda x:(-x[1],x[0]))
    
        
    
    
    #print(sorted_cnt)
    dict_result=dict(result.items())
    print(dict_result)
    
    for genre,_ in sorted_cnt:
        v=dict_result[genre]
        if len(v)==1:
            answer.append(v[0][0])
            
        else:
            answer.append(v[0][0])
            answer.append(v[1][0])

    return answer