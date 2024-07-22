import Foundation

func solution(_ park:[String], _ routes:[String]) -> [Int] {
    var park = park.map{Array($0)}
    
    var r = 0
    var c = 0
    
    for i in park {
        if i.contains("S") {
            let matrix = i.map{String($0)}
            c = matrix.firstIndex(of: "S")!
            break
        } else {
            r += 1
        }
    }
    
    let dic = ["E": 1, "S": 1, "N": -1, "W": -1]
    
    let rLimit = park.count - 1
    let cLimit = park[0].count - 1
    
    for move in routes {
        let a = move.split(separator: " ")
        let dir = String(a[0])
        let cnt = Int(a[1])!
        
        var isValue = true
        let realR = r
        let realC = c
        
        for _ in 0..<cnt {
            if dir == "E" || dir == "W" {
                if c + dic[dir]! >= 0 && c + dic[dir]! <= cLimit && park[r][c + dic[dir]!] != "X" {
                    c += dic[dir]!
                } else {
                    isValue = false
                    break
                }
            } else if dir == "N" || dir == "S" {
                if r + dic[dir]! >= 0 && r + dic[dir]! <= rLimit && park[r + dic[dir]!][c] != "X" {
                    r += dic[dir]!
                } else {
                    isValue = false
                    break
                }
            }
        }
        
        // 이동이 유효하지 않으면 원래 위치로 되돌리기
        if !isValue {
            r = realR
            c = realC
        }
    }
    
    return [r, c]
}
