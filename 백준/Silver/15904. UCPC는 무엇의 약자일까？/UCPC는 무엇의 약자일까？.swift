import Foundation

let input = readLine()!
let target = ["U", "C", "P", "C"]
var idx = 0

for char in input {
    if String(char) == target[idx] {
        idx += 1
        if idx == target.count {
            break
        }
    }
}

print(idx == target.count ? "I love UCPC" : "I hate UCPC")
