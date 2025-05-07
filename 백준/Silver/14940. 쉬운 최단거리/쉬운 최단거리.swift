import Foundation

// 입력 받기
let size = readLine()!.split(separator: " ").map { Int($0)! }
let n = size[0], m = size[1]

var maps: [[Int]] = []
var visited = Array(repeating: Array(repeating: -1, count: m), count: n)

var startX = 0
var startY = 0

for i in 0..<n {
    let row = readLine()!.split(separator: " ").map { Int($0)! }
    maps.append(row)
    if let index = row.firstIndex(of: 2) {
        startX = i
        startY = index
    }
}

// 방향 벡터 (상, 하, 좌, 우)
let dx = [-1, 1, 0, 0]
let dy = [0, 0, -1, 1]

// BFS
var queue = [(startX, startY)]
visited[startX][startY] = 0

while !queue.isEmpty {
    let (x, y) = queue.removeFirst()
    
    for k in 0..<4 {
        let nx = x + dx[k]
        let ny = y + dy[k]
        
        if nx >= 0 && nx < n && ny >= 0 && ny < m {
            if maps[nx][ny] == 1 && visited[nx][ny] == -1 {
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
            }
        }
    }
}

// 출력
for i in 0..<n {
    for j in 0..<m {
        if maps[i][j] == 0 {
            print(0, terminator: " ")
        } else {
            print(visited[i][j], terminator: " ")
        }
    }
    print()
}
