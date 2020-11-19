/*
We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.
*/
class Solution {
public:
    vector<int> decompressRLElist(vector<int>& nums) {
        vector<int> list;
        for(int i=0;i<nums.size();i+=2){
            for(int j=0; j<nums.at(i);j++){
                list.push_back(nums.at(i+1));
            }
        }
        return list;
    }
};
