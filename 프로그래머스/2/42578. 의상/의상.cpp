#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    
    unordered_map<string,int> wearing;
    for(auto x:clothes){
        wearing[x[1]]++;
    }
    
    for(auto x:wearing){
        x.second++;
        answer=answer*x.second;
    }
    
    
    return answer-1;
}