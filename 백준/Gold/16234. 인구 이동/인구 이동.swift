import Foundation


let nums = readLine()!.split(separator:" ").map{Int(String($0))!}

let n=nums[0]
let L=nums[1]
let R=nums[2]

var maps:[[Int]]=[]

for _ in 0..<n{
    let row = readLine()!.split(separator:" ").map{Int(String($0))!}
    maps.append(row)
}

//날짜
var days=0
var safe=true
let dx=[-1,1,0,0]
let dy=[0,0,-1,1]


func bfs(_ x:Int,_ y:Int,_ visited:inout [[Bool]],_ total:inout Int,_ location:inout [(Int,Int)]){
    var queue:[(Int,Int)]=[]
    location.append((x,y))
    total += maps[x][y]
    queue.append((x,y))
    visited[x][y]=true

    var id=0

    while id<queue.count{
        let (x,y) = queue[id]
        id+=1

        for k in 0..<4{
            let nx=x+dx[k]
            let ny=y+dy[k]

            if 0<=nx && nx<n && 0<=ny && ny<n{
                if !visited[nx][ny] && L <= abs(maps[nx][ny]-maps[x][y]) && abs(maps[nx][ny]-maps[x][y]) <= R{
                    visited[nx][ny]=true
                    queue.append((nx,ny))
                    total += maps[nx][ny]
                    location.append((nx,ny))
                }
            }
        }
    }
}


func check(_ x:Int,_ y:Int) ->Bool {
    for i in 0..<4{
        let nx=x+dx[i]
        let ny=y+dy[i]

        if 0<=nx && nx<n && 0<=ny && ny<n{
            if L <= abs(maps[nx][ny]-maps[x][y]) && abs(maps[nx][ny]-maps[x][y]) <= R{
                return true
            }
        }
    }
    return false
}


while safe{
    safe=false
    //possible , 즉 이제 불가능한데 날짜 추가 안하고 끝내버림
    var possible=false
    //하루마다 초기화 해야함

    //국경 연 나라의 좌표,
    var location:[(Int,Int)]=[]
    //국경 연 나라들의 총 인구수
    var total=0
    var visited=Array(repeating:Array(repeating:false,count:n),count:n)


    //여기서 bfs
    for i in 0..<n{
        for j in 0..<n{
            //방문한적 없고 그 상하좌우로 L<= v <=R 이라면 bfs수행
            if !visited[i][j] && check(i,j){
                bfs(i,j,&visited,&total,&location)
                safe=true
                possible=true
                //여기서 한번 다 뿌려줘야함
                let person = total/location.count
                //print(location)
                for (x,y) in location{
                    maps[x][y]=person
                }
                //다시 초기화
                //국경 연 나라의 좌표,
                location=[]
                //국경 연 나라들의 총 인구수
                total=0
            }
        }
    }
    if !possible{
        print(days)
        exit(0)
    }

    days+=1

}

print(days)
