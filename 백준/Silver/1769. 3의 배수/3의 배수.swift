import Foundation

var nums = readLine()!
//print(Array(nums))
var cnt=0

while nums.count != 1{
    var total=0
    var chars=Array(nums)

    for i in 0..<nums.count{
        total += Int(String(chars[i]))!
    }
    nums=String(total)
    cnt+=1
}

print(cnt)
var res = Int((nums))!
if res%3==0{
    print("YES")
}
else{
    print("NO")
}
