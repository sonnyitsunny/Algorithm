import Foundation

func solution(_ players:[String], _ callings:[String]) -> [String] {
    var result=players
    var order:[String:Int]=[:]
    //callings를 순회하면서 각 요소의 players 내의 인덱스를 구하고 구한인덱스에서 -1한 값과 현재 값을 교환한다.
    
    for (index,player) in result.enumerated(){
        order[player]=index
    }
    
    for name in callings{
        //이름 불린 애의 인덱스 저장
        var targetIndex = order[name]!
        //앞에 있는 애의 이름 저장
        var forwardName = result[targetIndex-1]
        
        result[targetIndex-1] = name
        result[targetIndex] = forwardName
        
        order[name]! -= 1
        order[forwardName]! += 1
    }
    
    
    
    
    return result
}