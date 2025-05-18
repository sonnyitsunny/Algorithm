
import sys
sys.setrecursionlimit(10**9)
# 1-> 3 -> 3 (3혼자)
#dfs 인자로 불렀을 때 애랑 걔가 연결된애를 넘겨준다.


# 2 -> 1 -> (막힘 visited)3 -> 3
#4->7 ->6 ->4

#
# 자기가 스스로 선택하면 혼자 팀
# 선택 시작해서 처음 시작한애까지 오면 걔네도 한팀

#case 완전 처음 호출한 애를 인자로 넘겨줘서  지금애가 누굴 가리키고 있는지 (처음호출한애 가리키면 끝
# 아니라면 계속 dfs 자기 자신이라면 끝

#한팀이 되면 결과리스트에 있는애를 다 인덱스로 사용해서 visited, 그리고 그 길이만큼 전체 학생수에서 뺴준다.

t=int(input())



def dfs(x):
    global cnt
    visited[x]=True
    next=graph[x]

    if not visited[next]:
        dfs(next)
    else:
        if not finished[next]:
            temp=next
            cnt+=1
            while temp!=x:
                temp=graph[temp]
                cnt+=1

    finished[x]=True

#4비짓 
#next 7
#dfs 7
#7 비짓
#next 6
#dfs 6
#6 비짓
#next 4
# temp 4
#cnt 1
#4 != 6
#temp 7
#cnt 2
# 7!= 6
# temp 6
#cnt 3
# 6 6
#6 피니쉬


for _ in range(t):
    
    n=int(input())
    visited=[False]*(n+1)
    finished=[False]*(n+1)
    graph=[0]
    graph.extend(list(map(int,input().split())))
    cnt=0
    #dfs(처음,호출한애)
    for i in range(1,n+1):
        if not visited[i]:
            dfs(i)

    print(n-cnt)

    
    