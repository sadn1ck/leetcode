/*
Given an array nums of integers, return how many of them contain an even number of digits. 
*/
class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int count = 0;
        for (auto num: nums){
            if ((int)(floor(log10(num)+ 1))%2 == 0 ){
                count++;
            }
        }
        return count;
    }
};
