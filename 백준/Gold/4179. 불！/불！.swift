//
//  main.swift
//  ps
//
//  Created by 손동현 on 5/15/25.
//

import Foundation

let input = readLine()!.split(separator:" ").map{Int($0)!}
let r=input[0], c=input[1]

let dx=[-1,1,0,0]
let dy=[0,0,-1,1]

var graph=[[Character]]()

var fire = Array(repeating: Array(repeating:-1,count:c),count:r)
var jihun = Array(repeating: Array(repeating: -1, count: c), count: r)

var fq=[(Int,Int)]()
var jq=[(Int,Int)]()


for _ in 0..<r{
    let row = Array(readLine()!)
    graph.append(row)
}

for i in 0..<r{
    for j in 0..<c{
        if graph[i][j]=="F"{
            fq.append((i,j))
            fire[i][j]=0
        }
        else if graph[i][j]=="J"{
            jq.append((i,j))
            jihun[i][j]=0
        }
    }
}

var fireIndex=0
while fireIndex<fq.count{
    let(x,y)=fq[fireIndex]
    fireIndex+=1

    for k in 0..<4{
        let nx = x+dx[k],ny=y+dy[k]

        if 0<=nx && nx<r && 0<=ny && ny<c{
            if graph[nx][ny] != "#" && fire[nx][ny] == -1{
                fire[nx][ny]=fire[x][y]+1
                fq.append((nx,ny))
            }
        }
    }
}


var jihunIndex=0
while jihunIndex<jq.count{
    let(x,y)=jq[jihunIndex]
    jihunIndex+=1


    if x==0 || x==r-1 || y==0 || y==c-1{
        print(jihun[x][y]+1)
        exit(0)
    }

    for k in 0..<4{
        let nx = x+dx[k],ny=y+dy[k]

        if 0<=nx && nx<r && 0<=ny && ny<c{
            if graph[nx][ny] != "#" && jihun[nx][ny] == -1 {
                if fire[nx][ny] == -1 || jihun[x][y] + 1 < fire[nx][ny]{
                    jihun[nx][ny]=jihun[x][y]+1
                    jq.append((nx,ny))
                }
            }
        }
    }

}
print("IMPOSSIBLE")
