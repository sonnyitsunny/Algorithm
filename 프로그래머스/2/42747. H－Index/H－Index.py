#오름차순 정렬하고 이분탐색이용해서 , h를 1부터 논문의 최대 수까지 반복문
# 1.h번 이상 인용된 논문 수 구할 때는 왼쪽으로 구하고 리스트길이 - 그 리턴 인덱스 가 갯수
# 2.h번 이하 인용된 논문 수 구하는 건 오른쪽으로 구하고 리스트 길이 - 그 리턴 인덱스가 갯수
#1과 2 조건을 둘 다 만족하는 건 결과 리스트에 넣어준다.
from bisect import bisect_left,bisect_right
def solution(citations):
    answer = []
    n=len(citations)
    
    citations.sort()
    h=max(citations)
    for i in range(0,h+1):
        up=n-bisect_left(citations,i)
        down=n-bisect_right(citations,i)
        if up>=i and down<=i:
            answer.append(i)
    

    return max(answer)