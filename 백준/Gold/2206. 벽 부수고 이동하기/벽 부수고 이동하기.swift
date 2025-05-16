import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let n = input[0], m = input[1]

var map: [[Int]] = []
for _ in 0..<n {
    map.append(readLine()!.map { Int(String($0))! })
}

var visited = Array(repeating: Array(repeating: [false, false], count: m), count: n)

let dx = [-1, 1, 0, 0]
let dy = [0, 0, -1, 1]

struct Node {
    let x: Int
    let y: Int
    let breakWall: Int // 0이면 벽 안 부숨, 1이면 벽 부숨
    let dist: Int
}

func bfs() -> Int {
    var queue = [Node]()
    queue.append(Node(x: 0, y: 0, breakWall: 0, dist: 1))
    visited[0][0][0] = true

    var index = 0

    while index < queue.count {
        let now = queue[index]
        index += 1

        if now.x == n - 1 && now.y == m - 1 {
            return now.dist
        }

        for i in 0..<4 {
            let nx = now.x + dx[i]
            let ny = now.y + dy[i]

            if nx < 0 || ny < 0 || nx >= n || ny >= m {
                continue
            }

            if map[nx][ny] == 0 && !visited[nx][ny][now.breakWall] {
                visited[nx][ny][now.breakWall] = true
                queue.append(Node(x: nx, y: ny, breakWall: now.breakWall, dist: now.dist + 1))
            }

            if map[nx][ny] == 1 && now.breakWall == 0 && !visited[nx][ny][1] {
                visited[nx][ny][1] = true
                queue.append(Node(x: nx, y: ny, breakWall: 1, dist: now.dist + 1))
            }
        }
    }

    return -1
}

print(bfs())
