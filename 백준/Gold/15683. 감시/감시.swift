import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let (n, m) = (input[0], input[1])
var map = [[Int]]()
var cctvs = [(Int, Int, Int)]()  // (x, y, type)

for i in 0..<n {
    let row = readLine()!.split(separator: " ").map { Int($0)! }
    for j in 0..<m {
        if 1...5 ~= row[j] {
            cctvs.append((i, j, row[j]))
        }
    }
    map.append(row)
}

// 상, 우, 하, 좌 (시계 방향)
let dx = [-1, 0, 1, 0]
let dy = [0, 1, 0, -1]

// 각 CCTV 타입별 가능한 방향 조합
let directions: [[[Int]]] = [
    [],                              // 0 (사용 안 함)
    [[0], [1], [2], [3]],            // 1번
    [[0, 2], [1, 3]],                // 2번
    [[0, 1], [1, 2], [2, 3], [3, 0]],// 3번
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], // 4번
    [[0, 1, 2, 3]]                   // 5번
]

var minBlind = Int.max

func watch(_ tempMap: inout [[Int]], _ x: Int, _ y: Int, _ dir: Int) {
    var nx = x + dx[dir]
    var ny = y + dy[dir]

    while nx >= 0 && nx < n && ny >= 0 && ny < m {
        if tempMap[nx][ny] == 6 { break } // 벽
        if tempMap[nx][ny] == 0 {
            tempMap[nx][ny] = -1 // 감시 영역
        }
        nx += dx[dir]
        ny += dy[dir]
    }
}

func dfs(_ depth: Int, _ tempMap: [[Int]]) {
    if depth == cctvs.count {
        let blindCount = tempMap.flatMap { $0 }.filter { $0 == 0 }.count
        minBlind = min(minBlind, blindCount)
        return
    }

    let (x, y, type) = cctvs[depth]

    for dirs in directions[type] {
        var copiedMap = tempMap
        for d in dirs {
            watch(&copiedMap, x, y, d)
        }
        dfs(depth + 1, copiedMap)
    }
}

dfs(0, map)
print(minBlind)
