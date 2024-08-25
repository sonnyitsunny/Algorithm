func solution(_ msg: String) -> [Int] {
    // 초기 사전 설정
    var dic: [String: Int] = [:]
    let alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    var dicIndex = 1
    
    for ch in alphabet {
        dic[String(ch)] = dicIndex
        dicIndex += 1
    }
    
    var result: [Int] = []
    var tmp = ""
    var i = 0
    let msgArray = Array(msg)
    
    while i < msgArray.count {
        tmp += String(msgArray[i]) // 현재 글자 추가
        i += 1
        
        // 다음 글자가 있으면 계속 추가해서 사전에 있는지 확인
        while i < msgArray.count && dic[tmp + String(msgArray[i])] != nil {
            tmp += String(msgArray[i])
            i += 1
        }
        
        // 사전에 있는 가장 긴 문자열의 색인 번호를 결과에 추가
        result.append(dic[tmp]!)
        
        // 새로운 문자열을 사전에 추가
        if i < msgArray.count {
            dic[tmp + String(msgArray[i])] = dicIndex
            dicIndex += 1
        }
        
        // tmp 초기화
        tmp = ""
    }
    
    return result
}
