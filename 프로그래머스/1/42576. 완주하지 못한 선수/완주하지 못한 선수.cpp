#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>
using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    
    unordered_map<string,int> player;
    
    for(string p : participant){
        player[p]++;
    }
    for(string c : completion){
        player[c]--;
    }
    
    for(auto x:player){
        if (x.second==1) {
            answer=x.first;
            break;
        }
    }
    
    
    
    return answer;
}