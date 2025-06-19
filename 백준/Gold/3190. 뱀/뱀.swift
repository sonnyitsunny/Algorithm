import Foundation

let n = Int(readLine()!)!
let k = Int(readLine()!)!

//0: 빈칸, 1: 사과, 2: 뱀
var board = Array(repeating: Array(repeating: 0, count: n), count: n)

for _ in 0..<k {
    let apple = readLine()!.split(separator: " ").map { Int($0)! }
    // 문제는 1-based
    board[apple[0]-1][apple[1]-1] = 1
}

// 방향 전환 정보 저장,시간: 방향
let l = Int(readLine()!)!
var directionChanges = [Int: String]()
for _ in 0..<l {
    let input = readLine()!.split(separator: " ")
    let time = Int(input[0])!
    let dir = String(input[1])
    directionChanges[time] = dir
}

// 방향 설정 (동남서북)
let dx = [0, 1, 0, -1]
let dy = [1, 0, -1, 0]
var direction = 0 // 시작 방향 동쪽

// 앞이 꼬리, 뒤가 머리)
var snake: [(Int, Int)] = [(0, 0)]
board[0][0] = 2 // 뱀이 있는 칸은 2로 표시

var time = 0

// 방향 전환 함수
func turn(_ dir: String) {
    if dir == "L" {
        direction = (direction + 3) % 4  // 왼쪽 회전
    } else if dir == "D" {
        direction = (direction + 1) % 4  // 오른쪽 회전
    }
}

// 시작
while true {
    time += 1

    // 현재 머리 위치
    let head = snake.last!
    let nx = head.0 + dx[direction]
    let ny = head.1 + dy[direction]

    // 벽 또는 자기 몸에 부딪히면 종료
    if nx < 0 || ny < 0 || nx >= n || ny >= n || board[nx][ny] == 2 {
        break
    }

    // 사과가 있다면: 머리만 늘리고 꼬리 안 줄임
    if board[nx][ny] == 1 {
        board[nx][ny] = 2
        snake.append((nx, ny))
    }
    // 사과 없으면: 머리 늘리고, 꼬리 줄임
    else {
        board[nx][ny] = 2
        snake.append((nx, ny))
        let tail = snake.removeFirst()
        board[tail.0][tail.1] = 0
    }

    // 방향 전환 체크
    if let d = directionChanges[time] {
        turn(d)
    }
}

print(time)
