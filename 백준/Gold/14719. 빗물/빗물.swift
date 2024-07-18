import Foundation

// 입력 받기
let input = readLine()!.split(separator: " ").map { Int($0)! }
let (H, W) = (input[0], input[1])
let heights = readLine()!.split(separator: " ").map { Int($0)! }

var left = 0
var right = W - 1
var leftMax = heights[left]
var rightMax = heights[right]
var totalWater = 0

while left < right {
    if heights[left] < heights[right] {
        left += 1
        leftMax = max(leftMax, heights[left])
        totalWater += max(0, leftMax - heights[left])
    } else {
        right -= 1
        rightMax = max(rightMax, heights[right])
        totalWater += max(0, rightMax - heights[right])
    }
}

print(totalWater)

