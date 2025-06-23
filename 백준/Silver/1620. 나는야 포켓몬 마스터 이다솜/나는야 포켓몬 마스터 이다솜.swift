import Foundation


let nums = readLine()!.split(separator:" ").map{Int(String($0))!}
let n = nums[0]
let m = nums[1]

var dic:[String:Int]=[:]
var arr:[String]=[]
arr=["0"]+arr



for i in 1...n{
    let pokket = readLine()!
    let lowpokket = pokket.lowercased()
    if let p = dic[lowpokket]{

    }
    else{
        dic[lowpokket]=i
        arr.append(pokket)
    }

}

for _ in 0..<m{
    let target = readLine()!
    if Int(target) != nil{
        let number = Int(target)!
        print(arr[number])
    }
    else{
        let lowtarget = target.lowercased()
        if let p = dic[lowtarget]{
            let value = p
            print(value)
        }
    }

}
