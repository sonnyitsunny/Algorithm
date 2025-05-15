import Foundation
let dx = [-1,1,0,0,0,0]
let dy = [0,0,-1,1,0,0]
let dz = [0,0,0,0,-1,1]

while true {
    let input = readLine()!.split(separator:" ").map { Int($0)! }
    let L = input[0], R = input[1], C = input[2]
    if L == 0 && R == 0 && C == 0 {
        break
    }

    var q = [(Int, Int, Int)]()
    var graph = [[[Character]]]()
    var visited = Array(
        repeating: Array(
            repeating: Array(repeating: -1, count: C),
            count: R),
        count: L
    )

    for l in 0..<L {
        var layer = [[Character]]()
        for _ in 0..<R {
            let row = Array(readLine()!)
            layer.append(row)
        }
        graph.append(layer)

        readLine()

    }

    for k in 0..<L{
        for i in 0..<R{
            for j in 0..<C{
                if graph[k][i][j] == "S"{
                    q.append((k,i,j))
                    visited[k][i][j]=0

                }
            }
        }
    }


    var escape = false
    var Index = 0
    while Index < q.count {
        let (z,x,y) = q[Index]
        Index += 1

        if graph[z][x][y] == "E" {
            print("Escaped in \(visited[z][x][y]) minute(s).")
            escape = true
            break
        }

        for k in 0..<6 {
            let nz = z + dz[k], nx = x + dx[k], ny = y + dy[k]
            if 0 <= nz, nz < L, 0 <= nx, nx < R, 0 <= ny, ny < C {
                if visited[nz][nx][ny] == -1 && graph[nz][nx][ny] != "#" {
                    q.append((nz,nx,ny))
                    visited[nz][nx][ny] = visited[z][x][y] + 1
                }
            }
        }
    }

    if !escape {
        print("Trapped!")
    }
}
