/*
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
*/


class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        
        vector<int> sum;
        long long prevSum=0;
        for(int i=0;i<nums.size();i++){
            prevSum = prevSum + nums.at(i);
            sum.push_back(prevSum);
        }
        return sum;
    }
};
