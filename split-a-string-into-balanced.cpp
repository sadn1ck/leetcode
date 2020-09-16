/*
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.
*/

class Solution {
public:
    int balancedStringSplit(string s) {
        int l = 0, r = 0, t = 0;
        for(auto c: s){
            if (c == 'L'){
                l++;
            }
            else {
                r++;
            }
            if (l == r ){
                t++;
                l=0;
                r=0;
            }
        }
        return t;
    }
};
