import Foundation


let nums = readLine()!.split(separator:" ").map{Int(String($0))!}

let N=nums[0]
let M=nums[1]

//주사위 위치 x,y
var x=nums[2]
var y=nums[3]
let k=nums[4]

var maps:[[Int]]=[]

for _ in 0..<N{
    let row = readLine()!.split(separator:" ").map{Int(String($0))!}
    maps.append(row)
}
//명령들
let command=readLine()!.split(separator:" ").map{Int(String($0))!}

//동 서 북 남
let dx=[0,0,-1,1]
let dy=[1,-1,0,0]

//주사위 , 인덱스 1 1은 항상 서로 같음 그게 바닥이다.
//가로
var A = [0,0,0]
//세로
var B = [0,0,0,0]


func rotation(_ c:Int){
    var tmp1=0

    if c==1{
        tmp1=A[0]
        A.removeFirst()
        A.append(B[3])
        B[3]=tmp1
        B[1]=A[1]

    }
    else if c==2{
        tmp1=A[2]
        A.removeLast()
        A.insert(B[3],at:0)
        B[3]=tmp1
        B[1]=A[1]

    }

    else if c==3{
        
        A[1]=B[0]
        B.insert(B[3],at:0)
        B.removeLast()

    }


    else{
        A[1]=B[2]
        tmp1=B[0]
        B.removeFirst()
        B.append(tmp1)

    }
}


for c in command{
    //c는 1base라서 인덱스에 -1 해줘야함
    let nx=x+dx[c-1]
    let ny=y+dy[c-1]
    if 0<=nx && nx<N && 0<=ny && ny<M{
        x=nx
        y=ny
        // 굴리는 거 구현
        rotation(c)

        //지도칸에 따른 조건 따지기
        if maps[x][y]==0{
            //주사위 바닥은 A[1]
            maps[x][y]=A[1]
            print(B[3])
        }
        else{
            A[1]=maps[x][y]
            B[1]=maps[x][y]
            maps[x][y]=0
            print(B[3])
        }
    }

    else{
        continue
    }



}
