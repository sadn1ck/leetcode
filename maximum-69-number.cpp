/*
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
*/
class Solution {
public:
    int maximum69Number (int num) {
        vector<int> all;
        all.push_back(num);
        string n = to_string(num);
        for(int i=0; i<n.length();i++){
            char orig = n[i];
            if(n[i] == '6'){
                n[i] = '9';
            } else {
                n[i] = '6';
            }
            all.push_back(stoi(n));
            cout << n << "\n";
            n[i] = orig;
        }
        return *max_element(all.begin(), all.end());
    }
};
