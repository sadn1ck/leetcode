/*
Given a binary string s (a string consisting only of '0' and '1's).

Return the number of substrings with all characters 1's.

Since the answer may be too large, return it modulo 10^9 + 7.
*/

class Solution {
public:
    int numSub(string s) {
        long long curr = 0;
        long long sum = 0;
        for (auto c: s){
            if (c == '1'){
                curr += 1;
                sum = sum + curr;
            }
            else {
                curr = 0;
            }
        }
        return sum % (long long)(1e9 + 7);
    }
};
