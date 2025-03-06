def solution(sizes):
    answer = 0
    #sizes 반복문 돌아서 안에 내부 배열을 [작은거, 큰거]로 만든다
    #그리고 다시 반복문해서 0번인덱스에서 max값, 1번 인덱스에서 Max값 찾아냄
    x=0
    y=0
    for i in sizes:
        i.sort()
        x=max(i[0],x)
        y=max(i[1],y)
    
    answer=x*y
    return answer