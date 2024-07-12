import Foundation
//사진 별로 추억점수
//사진 속에 나오는 인물의 그리움 점수를 모두 합산한 값이 해당 사진의 추억 점수
func solution(_ name:[String], _ yearning:[Int], _ photo:[[String]]) -> [Int] {
    
    var result:[Int]=[]
    var nameScore:[String:Int]=[:]
    //딕셔너리로 이름별 추억점수 자료구조 만듬
    for i in 0..<name.count{
        nameScore[name[i]]=yearning[i]
    }
    
    
    //포토를 순회하면서 요소 안에 있는 이름을 딕셔너리에 있는 지 확인하고 점수를 합산
    for p in photo{
        var score = 0
        for i in 0..<p.count{
            if let _ = nameScore[p[i]]{
                score+=nameScore[p[i]]!
            }
            
            
        }
        result.append(score)
    }
    
    
    
    return result
}