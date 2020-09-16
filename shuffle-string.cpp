/*
Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.
*/
class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        int len = *max_element(indices.begin(), indices.end()) + 1;
        char restored[len];
        for (int i= 0; i< indices.size();i++){
            restored[indices[i]] = s[i];
        }
        string st ="";
        for(auto c: restored){
            cout <<c;
            st = st + c;
        }
        return st;
    }
};
