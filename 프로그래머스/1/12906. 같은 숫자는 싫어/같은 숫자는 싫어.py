def solution(arr):
    answer = []
    #arr만큼 반복문
    # 배열에 넣고 i인덱스에 다음게 있는지 확인있으면 컨티뉴, 없다면 그배열에 집어넣고 컨티뉴, 해서 바뀌었으면 결과 배열에 집어넣고 임시배열에도 집어넣음
    temp=[]
    temp.append(arr[0])
    for i in range(1,len(arr)):
        if temp[-1] != arr[i]:
            temp.append(arr[i])
        else:
            continue
    
    return temp