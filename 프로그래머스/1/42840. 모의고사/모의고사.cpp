#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    
    vector<int> p1 = {1, 2, 3, 4, 5};
    vector<int> p2 = {2, 1, 2, 3, 2, 4, 2, 5};
    vector<int> p3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    
    int ps1 = 0;
    int ps2 = 0;
    int ps3 = 0;
    
    int n = answers.size();
    for(int i=0;i<n;i++){
        if (answers[i]==p1[i%p1.size()]){
            ps1++;
        }
        
        if (answers[i]==p2[i%p2.size()]){
            ps2++;
        }
        if (answers[i]==p3[i%p3.size()]){
            ps3++;
        }
    }
    int max_v = 0;
    max_v=max({ps1,ps2,ps3});
    if (max_v==ps1){
        answer.push_back(1);
    }
    if (max_v==ps2){
        answer.push_back(2);
    }
    if (max_v==ps3){
        answer.push_back(3);
    }
    
        
        return answer;
}