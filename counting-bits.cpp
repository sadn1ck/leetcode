/*
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array. 
*/

class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> counts;
        for(int i=0;i<=num;i++){
            counts.push_back(__builtin_popcount(i));
        }
    return counts;
    }
};
