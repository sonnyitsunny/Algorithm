import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let n = input[0], m = input[1]


var switchMap = Array(repeating: Array(repeating: [(Int, Int)](), count: n + 1), count: n + 1)
var isOn = Array(repeating: Array(repeating: false, count: n + 1), count: n + 1)
var visited = Array(repeating: Array(repeating: false, count: n + 1), count: n + 1)

let dx = [-1, 1, 0, 0]
let dy = [0, 0, -1, 1]

for _ in 0..<m {
    let line = readLine()!.split(separator: " ").map { Int($0)! }
    let (x, y, a, b) = (line[0], line[1], line[2], line[3])
    switchMap[x][y].append((a, b))
}
isOn[1][1] = true
visited[1][1] = true
var queue = [(1, 1)]
var idx = 0

while idx < queue.count {
    let (x, y) = queue[idx]
    idx += 1

    
    for (a, b) in switchMap[x][y] {
        if !isOn[a][b] {
            isOn[a][b] = true
            for i in 0..<4 {
                let nx = a + dx[i]
                let ny = b + dy[i]
                if 1 <= nx, nx <= n, 1 <= ny, ny <= n {
                    if visited[nx][ny] {
                        visited[a][b] = true
                        queue.append((a, b))
                        break
                    }
                }
            }
        }
    }

    
    for i in 0..<4 {
        let nx = x + dx[i]
        let ny = y + dy[i]

        if 1 <= nx, nx <= n, 1 <= ny, ny <= n {
            if isOn[nx][ny] && !visited[nx][ny] {
                visited[nx][ny] = true
                queue.append((nx, ny))
            }
        }
    }
}

// 불켜진 방세기
var result = 0
for i in 1...n {
    for j in 1...n {
        if isOn[i][j] {
            result += 1
        }
    }
}
print(result)
